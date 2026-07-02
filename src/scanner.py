from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf


IST = ZoneInfo("Asia/Kolkata")

NIFTY50_CSV_URL = "https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv"

FALLBACK_SYMBOLS = {
    "RELIANCE.NS": "Reliance Industries",
    "TCS.NS": "Tata Consultancy Services",
    "INFY.NS": "Infosys",
    "HDFCBANK.NS": "HDFC Bank",
    "ICICIBANK.NS": "ICICI Bank",
    "LT.NS": "Larsen & Toubro",
    "SBIN.NS": "State Bank of India",
    "BHARTIARTL.NS": "Bharti Airtel",
    "ITC.NS": "ITC",
    "AXISBANK.NS": "Axis Bank",
}

BENCHMARK_SYMBOL = "^NSEI"

def get_nifty50_symbols() -> tuple[dict, str]:
    """
    Fetch Nifty 50 constituents from the official NSE/Nifty Indices CSV.
    If the fetch fails, fall back to the beginner test universe.
    """
    try:
        constituents = pd.read_csv(NIFTY50_CSV_URL)

        if "Symbol" not in constituents.columns or "Company Name" not in constituents.columns:
            return FALLBACK_SYMBOLS, "Fallback test universe; official CSV format not recognized"

        symbols = {}

        for _, row in constituents.iterrows():
            nse_symbol = str(row["Symbol"]).strip()
            company = str(row["Company Name"]).strip()

            if nse_symbol:
                symbols[f"{nse_symbol}.NS"] = company

        if len(symbols) < 45:
            return FALLBACK_SYMBOLS, "Fallback test universe; official CSV returned too few symbols"

        return symbols, "Official NSE/Nifty Indices Nifty 50 CSV"

    except Exception as exc:
        return FALLBACK_SYMBOLS, f"Fallback test universe; official Nifty 50 CSV fetch failed: {exc}"
def download_price_data(symbol: str, period: str = "1y") -> pd.DataFrame:
    data = yf.download(
        symbol,
        period=period,
        interval="1d",
        progress=False,
        auto_adjust=False,
    )

    if data.empty:
        return data

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data.dropna()


def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def atr(data: pd.DataFrame, period: int = 14) -> pd.Series:
    high_low = data["High"] - data["Low"]
    high_close = (data["High"] - data["Close"].shift()).abs()
    low_close = (data["Low"] - data["Close"].shift()).abs()

    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return true_range.rolling(period).mean()


def add_indicators(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()
    data["EMA20"] = ema(data["Close"], 20)
    data["EMA50"] = ema(data["Close"], 50)
    data["EMA200"] = ema(data["Close"], 200)
    data["RSI14"] = rsi(data["Close"], 14)
    data["ATR14"] = atr(data, 14)
    data["AvgVol20"] = data["Volume"].rolling(20).mean()
    return data.dropna()


def get_benchmark_context() -> dict:
    data = download_price_data(BENCHMARK_SYMBOL, "1y")

    if data.empty or len(data) < 220:
        return {
            "available": False,
            "return_percent": 0.0,
            "market_condition": "Benchmark data unavailable",
            "notes": "Nifty benchmark data could not be verified.",
        }

    data = add_indicators(data)
    latest = data.iloc[-1]
    previous = data.iloc[-2]

    close = float(latest["Close"])
    prev_close = float(previous["Close"])
    return_percent = ((close - prev_close) / prev_close) * 100

    above_ema20 = close > float(latest["EMA20"])
    above_ema50 = close > float(latest["EMA50"])
    ema20_above_ema50 = float(latest["EMA20"]) > float(latest["EMA50"])

    if above_ema20 and above_ema50 and ema20_above_ema50 and return_percent > 0:
        market_condition = "Bullish to selective swing environment"
    elif above_ema20 and above_ema50:
        market_condition = "Selective swing environment"
    elif close < float(latest["EMA20"]):
        market_condition = "Risky environment; avoid aggressive fresh longs"
    else:
        market_condition = "Neutral / data-limited environment"

    return {
        "available": True,
        "close": round(close, 2),
        "return_percent": round(return_percent, 2),
        "ema20": round(float(latest["EMA20"]), 2),
        "ema50": round(float(latest["EMA50"]), 2),
        "market_condition": market_condition,
        "notes": "Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.",
    }


def get_rejection_reasons(flags: dict) -> list[str]:
    reasons = []

    if not flags["technical_pass"]:
        reasons.append("Technical trend failed: price/EMA structure is not clean.")

    if not flags["momentum_pass"]:
        reasons.append("Momentum failed: RSI is outside preferred 55-70 range.")

    if not flags["volume_pass"]:
        reasons.append("Volume failed: volume is not above 1.5x 20-day average volume.")

    if not flags["relative_strength_pass"]:
        reasons.append("Relative strength failed: stock did not outperform Nifty.")

    if not flags["not_overextended"]:
        reasons.append("Overextension risk: price is too far from EMA20 or RSI is too high.")

    if not flags["risk_reward_pass"]:
        reasons.append("Risk-reward failed: setup does not offer minimum 1:2 risk-reward.")

    return reasons


def build_red_team_note(result: dict) -> list[str]:
    notes = []

    if result["volume_pass"] is False:
        notes.append("Main objection: volume confirmation is weak, so breakout/follow-through may fail.")

    if result["momentum_pass"] is False:
        if result["rsi14"] > 70:
            notes.append("Momentum caution: RSI is above the preferred range, so chasing may be risky.")
        else:
            notes.append("Momentum caution: RSI is not strong enough for a clean swing setup.")

    if result["relative_strength_pass"] is False:
        notes.append("Relative strength concern: the stock is not clearly outperforming Nifty.")

    if result["not_overextended"] is False:
        notes.append("Overextension concern: entry may be late; wait for pullback or fresh confirmation.")

    if result["risk_reward_pass"] is False:
        notes.append("Trade-plan concern: target versus stop-loss does not justify the risk.")

    if not notes:
        notes.append("No major technical objection found in MVP filters, but manual chart/news confirmation is still required.")

    notes.append("Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.")

    return notes


def analyze_symbol(symbol: str, company: str, nifty_return: float) -> dict | None:
    data = download_price_data(symbol, "1y")

    if data.empty or len(data) < 220:
        return None

    data = add_indicators(data)

    if len(data) < 30:
        return None

    latest = data.iloc[-1]
    previous = data.iloc[-2]

    close = float(latest["Close"])
    high = float(latest["High"])
    low = float(latest["Low"])
    previous_close = float(previous["Close"])

    ema20 = float(latest["EMA20"])
    ema50 = float(latest["EMA50"])
    ema200 = float(latest["EMA200"])
    rsi14 = float(latest["RSI14"])
    atr14 = float(latest["ATR14"])
    volume = float(latest["Volume"])
    avg_vol20 = float(latest["AvgVol20"])

    previous_20_days = data.iloc[-21:-1]
    nearest_resistance = float(previous_20_days["High"].max())
    nearest_support = float(previous_20_days["Low"].min())

    stock_return = ((close - previous_close) / previous_close) * 100
    relative_strength = stock_return - nifty_return

    technical_pass = close > ema20 and close > ema50 and ema20 > ema50
    momentum_pass = 55 <= rsi14 <= 70
    volume_pass = volume > 1.5 * avg_vol20
    relative_strength_pass = relative_strength > 0
    not_overextended = close <= ema20 * 1.08 and rsi14 <= 75

    stop_loss = max(nearest_support, close - (1.5 * atr14))
    risk_per_share = close - stop_loss

    if close > nearest_resistance:
        setup_type = "Breakout / momentum continuation"
        target_1 = close + (2 * risk_per_share)
    else:
        setup_type = "Trend watchlist / below resistance"
        target_1 = nearest_resistance

    reward_per_share = target_1 - close
    risk_reward = reward_per_share / risk_per_share if risk_per_share > 0 else 0
    risk_reward_pass = risk_reward >= 2

    flags = {
        "technical_pass": technical_pass,
        "momentum_pass": momentum_pass,
        "volume_pass": volume_pass,
        "relative_strength_pass": relative_strength_pass,
        "not_overextended": not_overextended,
        "risk_reward_pass": risk_reward_pass,
    }

    rejection_reasons = get_rejection_reasons(flags)

    qualified = all(flags.values())

    score = 0
    score += 25 if technical_pass else 0
    score += 20 if volume_pass else 0
    score += 15 if momentum_pass else 0
    score += 15 if relative_strength_pass else 0
    score += 15 if risk_reward_pass else 0
    score += 10 if close > ema200 and not_overextended else 0

    result = {
        "symbol": symbol,
        "company": company,
        "close": round(close, 2),
        "high": round(high, 2),
        "low": round(low, 2),
        "volume": int(volume),
        "avg_volume_20": int(avg_vol20),
        "ema20": round(ema20, 2),
        "ema50": round(ema50, 2),
        "ema200": round(ema200, 2),
        "rsi14": round(rsi14, 2),
        "atr14": round(atr14, 2),
        "nearest_support": round(nearest_support, 2),
        "nearest_resistance": round(nearest_resistance, 2),
        "stock_return_percent": round(stock_return, 2),
        "relative_strength_vs_nifty": round(relative_strength, 2),
        "setup_type": setup_type,
        "buy_zone": f"Near {round(close, 2)} only after price confirmation",
        "stop_loss": round(stop_loss, 2),
        "target_1": round(target_1, 2),
        "risk_per_share": round(risk_per_share, 2),
        "reward_per_share": round(reward_per_share, 2),
        "risk_reward": round(risk_reward, 2),
        "score": score,
        "qualified": qualified,
        "rejection_reasons": rejection_reasons,
        **flags,
    }

    result["red_team_notes"] = build_red_team_note(result)
    return result


def yes_no(value: bool) -> str:
    return "Yes" if value else "No"


def create_report(results: list[dict], benchmark: dict, universe_name: str, universe_source: str) -> str:
    now_ist = datetime.now(IST).strftime("%Y-%m-%d %H:%M IST")
    report_date = datetime.now(IST).strftime("%Y-%m-%d")

    verified_count = len(results)
    final_candidates = [r for r in results if r["qualified"]]
    watchlist = [
    r for r in results
    if not r["qualified"]
    and r["technical_pass"]
    and sum([
        r["momentum_pass"],
        r["volume_pass"],
        r["relative_strength_pass"],
        r["risk_reward_pass"],
        r["not_overextended"],
    ]) >= 2
]
    rejected = [
    r for r in results
    if not r["qualified"] and r not in watchlist
]

    lines = []

    lines.append("# NSE Swing Scanner Report")
    lines.append("")
    lines.append(f"Report date: {report_date}")
    lines.append(f"Run time: {now_ist}")
   lines.append(f"Universe intended: {universe_name}")
lines.append(f"Universe source: {universe_source}")
    lines.append(f"Stocks verified: {verified_count}")
    lines.append(f"Market condition: {benchmark['market_condition']}")
    lines.append("Data confidence: Medium")
    lines.append("Report status: Technical MVP / Data-limited")
    lines.append("")

    lines.append("## Benchmark Context")
    if benchmark["available"]:
        lines.append(f"- Nifty close: {benchmark['close']}")
        lines.append(f"- Nifty return: {benchmark['return_percent']}%")
        lines.append(f"- Nifty EMA20: {benchmark['ema20']}")
        lines.append(f"- Nifty EMA50: {benchmark['ema50']}")
    else:
        lines.append("- Nifty benchmark data unavailable.")
    lines.append(f"- Note: {benchmark['notes']}")
    lines.append("")

    lines.append("## Scan Funnel")
    lines.append(f"- Stocks with verified OHLC: {verified_count}")
    lines.append(f"- Stocks with computed EMA/RSI/ATR: {verified_count}")
    lines.append(f"- Passed technical filter: {sum(1 for r in results if r['technical_pass'])}")
    lines.append(f"- Passed momentum filter: {sum(1 for r in results if r['momentum_pass'])}")
    lines.append(f"- Passed volume filter: {sum(1 for r in results if r['volume_pass'])}")
    lines.append(f"- Passed relative strength filter: {sum(1 for r in results if r['relative_strength_pass'])}")
    lines.append(f"- Passed risk-reward filter: {sum(1 for r in results if r['risk_reward_pass'])}")
    lines.append(f"- Final qualified candidates: {len(final_candidates)}")
    lines.append("")

    lines.append("## Executive Summary")
    if final_candidates:
        lines.append(f"{len(final_candidates)} stock(s) passed all MVP technical filters. These are research candidates only and still require manual chart, delivery, news, and event-risk confirmation.")
    else:
        lines.append("No clean qualified swing-trading candidate found today under the defined MVP rules.")
        lines.append("The system did not force recommendations. Watchlist names are not buy calls.")
    lines.append("")

    lines.append("## Final Qualified Candidates")

    if not final_candidates:
        lines.append("")
        lines.append("No clean qualified swing-trading candidate found today under the defined rules.")
    else:
        for r in sorted(final_candidates, key=lambda x: x["score"], reverse=True):
            lines.append("")
            lines.append(f"### {r['company']} ({r['symbol']})")
            lines.append(f"- Setup type: {r['setup_type']}")
            lines.append(f"- Close: {r['close']}")
            lines.append(f"- Buy zone: {r['buy_zone']}")
            lines.append(f"- Stop-loss: {r['stop_loss']}")
            lines.append(f"- Target 1: {r['target_1']}")
            lines.append(f"- Risk-reward: {r['risk_reward']}")
            lines.append(f"- Score: {r['score']}/100")
            lines.append("")
            lines.append("Evidence:")
            lines.append(f"- EMA20: {r['ema20']}, EMA50: {r['ema50']}, EMA200: {r['ema200']}")
            lines.append(f"- RSI14: {r['rsi14']}")
            lines.append(f"- Volume: {r['volume']}, AvgVol20: {r['avg_volume_20']}")
            lines.append(f"- Relative strength vs Nifty: {r['relative_strength_vs_nifty']}%")
            lines.append("")
            lines.append("IQ200 Red-Team Review:")
            for note in r["red_team_notes"]:
                lines.append(f"- {note}")

    lines.append("")
    lines.append("## Watchlist / Manual Review Only")

    if not watchlist:
        lines.append("No watchlist candidates.")
    else:
        for r in sorted(watchlist, key=lambda x: x["score"], reverse=True):
            lines.append("")
            lines.append(f"### {r['company']} ({r['symbol']})")
            lines.append(f"- Score: {r['score']}/100")
            lines.append(f"- Close: {r['close']}")
            lines.append(f"- Setup type: {r['setup_type']}")
            lines.append(f"- RSI14: {r['rsi14']}")
            lines.append(f"- Volume vs AvgVol20: {r['volume']} vs {r['avg_volume_20']}")
            lines.append(f"- Relative strength vs Nifty: {r['relative_strength_vs_nifty']}%")
            lines.append(f"- Nearest support: {r['nearest_support']}")
            lines.append(f"- Nearest resistance: {r['nearest_resistance']}")
            lines.append(f"- Stop-loss: {r['stop_loss']}")
            lines.append(f"- Target 1: {r['target_1']}")
            lines.append(f"- Risk-reward: {r['risk_reward']}")
            lines.append("")
            lines.append("Pass/Fail:")
            lines.append(f"- Technical pass: {yes_no(r['technical_pass'])}")
            lines.append(f"- Momentum pass: {yes_no(r['momentum_pass'])}")
            lines.append(f"- Volume pass: {yes_no(r['volume_pass'])}")
            lines.append(f"- Relative strength pass: {yes_no(r['relative_strength_pass'])}")
            lines.append(f"- Not overextended: {yes_no(r['not_overextended'])}")
            lines.append(f"- Risk-reward pass: {yes_no(r['risk_reward_pass'])}")
            lines.append("")
            lines.append("Why not a final candidate:")
            for reason in r["rejection_reasons"]:
                lines.append(f"- {reason}")
            lines.append("")
            lines.append("IQ200 Red-Team Review:")
            for note in r["red_team_notes"]:
                lines.append(f"- {note}")

    lines.append("")
    lines.append("## Rejected Stocks")

    if not rejected:
        lines.append("No low-score rejected stocks in this MVP universe.")
    else:
        for r in sorted(rejected, key=lambda x: x["score"], reverse=True):
            reason_text = "; ".join(r["rejection_reasons"]) if r["rejection_reasons"] else "Failed combined MVP filters."
            lines.append(f"- {r['company']} ({r['symbol']}): Score {r['score']}/100. {reason_text}")

    lines.append("")
    lines.append("## Full Scan Table")
    lines.append("")
    lines.append("| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |")
    lines.append("|---|---:|---:|---|---|---|---:|---:|---|")

    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        lines.append(
            f"| {r['symbol']} | {r['close']} | {r['score']} | "
            f"{yes_no(r['technical_pass'])} | {yes_no(r['momentum_pass'])} | "
            f"{yes_no(r['volume_pass'])} | {r['relative_strength_vs_nifty']}% | "
            f"{r['risk_reward']} | {yes_no(r['qualified'])} |"
        )

    lines.append("")
    lines.append("## Data Limitations")
    lines.append("- This MVP uses free public data through yfinance.")
    lines.append("- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.")
    lines.append("- Relative strength is based only on one-day stock return versus one-day Nifty return.")
    lines.append("- Support/resistance is approximated using the previous 20 trading days.")
    lines.append("- Use this report for research only.")
    lines.append("")
    lines.append("This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.")

    return "\n".join(lines)


def main() -> None:
    benchmark = get_benchmark_context()
    nifty_return = benchmark["return_percent"] if benchmark["available"] else 0.0

    results = []

    for symbol, company in SYMBOLS.items():
        try:
            result = analyze_symbol(symbol, company, nifty_return)
            if result:
                results.append(result)
        except Exception as exc:
            print(f"Failed for {symbol}: {exc}")

    report = create_report(results, benchmark)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / f"nse_swing_report_{datetime.now(IST).strftime('%Y-%m-%d')}.md"
    report_file.write_text(report, encoding="utf-8")

    print(report)


if __name__ == "__main__":
    main()
