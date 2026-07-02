
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


SYMBOLS = {
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


def analyze_symbol(symbol: str, company: str) -> dict | None:
    data = yf.download(symbol, period="1y", interval="1d", progress=False, auto_adjust=False)

    if data.empty or len(data) < 220:
        return None

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.dropna()

    data["EMA20"] = ema(data["Close"], 20)
    data["EMA50"] = ema(data["Close"], 50)
    data["EMA200"] = ema(data["Close"], 200)
    data["RSI14"] = rsi(data["Close"], 14)
    data["ATR14"] = atr(data, 14)
    data["AvgVol20"] = data["Volume"].rolling(20).mean()

    latest = data.iloc[-1]
    previous = data.iloc[-2]

    close = float(latest["Close"])
    ema20 = float(latest["EMA20"])
    ema50 = float(latest["EMA50"])
    ema200 = float(latest["EMA200"])
    rsi14 = float(latest["RSI14"])
    atr14 = float(latest["ATR14"])
    volume = float(latest["Volume"])
    avg_vol20 = float(latest["AvgVol20"])

    twenty_day_high = float(data["High"].tail(20).max())
    twenty_day_low = float(data["Low"].tail(20).min())

    stock_return = ((close - float(previous["Close"])) / float(previous["Close"])) * 100

    technical_pass = close > ema20 and close > ema50 and ema20 > ema50
    momentum_pass = 55 <= rsi14 <= 70
    volume_pass = volume > 1.5 * avg_vol20
    not_overextended = close <= ema20 * 1.08

    stop_loss = max(twenty_day_low, close - (1.5 * atr14))
    risk = close - stop_loss
    target_1 = close + (2 * risk)
    risk_reward = 2.0 if risk > 0 else 0

    qualified = all([
        technical_pass,
        momentum_pass,
        volume_pass,
        not_overextended,
        risk > 0,
        risk_reward >= 2,
    ])

    score = 0
    score += 30 if technical_pass else 0
    score += 20 if volume_pass else 0
    score += 15 if momentum_pass else 0
    score += 15 if risk_reward >= 2 else 0
    score += 10 if close > ema200 else 0
    score += 10 if not_overextended else 0

    return {
        "symbol": symbol,
        "company": company,
        "close": round(close, 2),
        "volume": int(volume),
        "avg_volume_20": int(avg_vol20),
        "ema20": round(ema20, 2),
        "ema50": round(ema50, 2),
        "ema200": round(ema200, 2),
        "rsi14": round(rsi14, 2),
        "atr14": round(atr14, 2),
        "twenty_day_high": round(twenty_day_high, 2),
        "twenty_day_low": round(twenty_day_low, 2),
        "stock_return_percent": round(stock_return, 2),
        "stop_loss": round(stop_loss, 2),
        "target_1": round(target_1, 2),
        "risk_reward": risk_reward,
        "score": score,
        "qualified": qualified,
        "technical_pass": technical_pass,
        "momentum_pass": momentum_pass,
        "volume_pass": volume_pass,
        "not_overextended": not_overextended,
    }


def create_report(results: list[dict]) -> str:
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    verified_count = len(results)
    final_candidates = [r for r in results if r["qualified"]]
    watchlist = [r for r in results if not r["qualified"] and r["score"] >= 60]

    lines = []
    lines.append("# NSE Swing Scanner Report")
    lines.append("")
    lines.append(f"Run time: {today}")
    lines.append("Universe intended: Beginner test universe")
    lines.append(f"Stocks verified: {verified_count}")
    lines.append("Data confidence: Medium")
    lines.append("Report status: Technical MVP / Data-limited")
    lines.append("")
    lines.append("## Scan Funnel")
    lines.append(f"- Stocks with verified OHLC: {verified_count}")
    lines.append(f"- Stocks with computed EMA/RSI/ATR: {verified_count}")
    lines.append(f"- Final qualified candidates: {len(final_candidates)}")
    lines.append("")
    lines.append("## Final Qualified Candidates")

    if not final_candidates:
        lines.append("")
        lines.append("No clean qualified swing-trading candidate found today under the defined rules.")
    else:
        for r in sorted(final_candidates, key=lambda x: x["score"], reverse=True):
            lines.append("")
            lines.append(f"### {r['company']} ({r['symbol']})")
            lines.append(f"- Close: {r['close']}")
            lines.append(f"- Buy zone: near {r['close']}")
            lines.append(f"- Stop-loss: {r['stop_loss']}")
            lines.append(f"- Target 1: {r['target_1']}")
            lines.append(f"- Risk-reward: {r['risk_reward']}")
            lines.append(f"- Score: {r['score']}/100")
            lines.append("")
            lines.append("Evidence:")
            lines.append(f"- EMA20: {r['ema20']}, EMA50: {r['ema50']}, EMA200: {r['ema200']}")
            lines.append(f"- RSI14: {r['rsi14']}")
            lines.append(f"- Volume: {r['volume']}, AvgVol20: {r['avg_volume_20']}")
            lines.append("")
            lines.append("IQ200 Red-Team Review:")
            lines.append("- This candidate still requires manual chart confirmation.")
            lines.append("- Avoid entry if the stock opens with a large gap-up or market direction turns weak.")
            lines.append("- This is not a guaranteed buy recommendation.")

    lines.append("")
    lines.append("## Watchlist")
    if not watchlist:
        lines.append("No watchlist candidates.")
    else:
        for r in sorted(watchlist, key=lambda x: x["score"], reverse=True):
            lines.append(f"- {r['company']} ({r['symbol']}): Score {r['score']}/100, RSI {r['rsi14']}, Close {r['close']}")

    lines.append("")
    lines.append("## Data Limitations")
    lines.append("- This MVP uses free public data through yfinance.")
    lines.append("- Delivery percentage, official NSE bhavcopy, fundamentals, and news checks are not included yet.")
    lines.append("- Use this report for research only.")
    lines.append("")
    lines.append("This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.")

    return "\n".join(lines)


def main() -> None:
    results = []

    for symbol, company in SYMBOLS.items():
        try:
            result = analyze_symbol(symbol, company)
            if result:
                results.append(result)
        except Exception as exc:
            print(f"Failed for {symbol}: {exc}")

    report = create_report(results)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / f"nse_swing_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    report_file.write_text(report, encoding="utf-8")

    print(report)


if __name__ == "__main__":
    main()
