# NSE Swing Scanner Report

Report date: 2026-07-17
Run time: 2026-07-17 20:18 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24334.3
- Nifty return: 1.09%
- Nifty EMA20: 24067.52
- Nifty EMA50: 23974.4
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 6
- Passed volume filter: 1
- Passed relative strength filter: 7
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 80/100
- Close: 1444.3
- Setup type: Breakout / momentum continuation
- RSI14: 65.95
- Volume vs AvgVol20: 11106912 vs 11997569
- Relative strength vs Nifty: 0.75%
- Nearest support: 1331.5
- Nearest resistance: 1433.0
- Stop-loss: 1405.5
- Target 1: 1521.89
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: No
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: Yes

Why not a final candidate:
- Volume failed: volume is not above 1.5x 20-day average volume.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### HDFC Bank (HDFCBANK.NS)
- Score: 55/100
- Close: 819.6
- Setup type: Trend watchlist / below resistance
- RSI14: 59.31
- Volume vs AvgVol20: 17412764 vs 32074083
- Relative strength vs Nifty: 0.31%
- Nearest support: 772.55
- Nearest resistance: 843.0
- Stop-loss: 797.67
- Target 1: 843.0
- Risk-reward: 1.07

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: No
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Volume failed: volume is not above 1.5x 20-day average volume.
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### State Bank of India (SBIN.NS)
- Score: 50/100
- Close: 1044.3
- Setup type: Trend watchlist / below resistance
- RSI14: 52.93
- Volume vs AvgVol20: 8450615 vs 10226733
- Relative strength vs Nifty: 0.18%
- Nearest support: 1011.4
- Nearest resistance: 1059.8
- Stop-loss: 1015.28
- Target 1: 1059.8
- Risk-reward: 0.53

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: No
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Volume failed: volume is not above 1.5x 20-day average volume.
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Momentum caution: RSI is not strong enough for a clean swing setup.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Bharti Airtel (BHARTIARTL.NS)
- Score: 40/100
- Close: 1908.8
- Setup type: Trend watchlist / below resistance
- RSI14: 62.82
- Volume vs AvgVol20: 4715357 vs 6074781
- Relative strength vs Nifty: -1.77%
- Nearest support: 1833.1
- Nearest resistance: 1966.0
- Stop-loss: 1852.83
- Target 1: 1966.0
- Risk-reward: 1.02

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: No
- Relative strength pass: No
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Volume failed: volume is not above 1.5x 20-day average volume.
- Relative strength failed: stock did not outperform Nifty.
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Relative strength concern: the stock is not clearly outperforming Nifty.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Rejected Stocks
- Tata Consultancy Services (TCS.NS): Score 45/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 45/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1444.3 | 80 | Yes | Yes | No | 0.75% | 2.0 | No |
| HDFCBANK.NS | 819.6 | 55 | Yes | Yes | No | 0.31% | 1.07 | No |
| SBIN.NS | 1044.3 | 50 | Yes | No | No | 0.18% | 0.53 | No |
| TCS.NS | 2269.0 | 45 | No | Yes | No | 2.0% | 2.0 | No |
| AXISBANK.NS | 1328.5 | 45 | No | No | Yes | 0.51% | 1.97 | No |
| BHARTIARTL.NS | 1908.8 | 40 | Yes | Yes | No | -1.77% | 1.02 | No |
| RELIANCE.NS | 1327.2 | 30 | No | Yes | No | 1.27% | 0.54 | No |
| INFY.NS | 1096.5 | 30 | No | Yes | No | 0.21% | 0.37 | No |
| LT.NS | 3814.5 | 15 | No | No | No | -0.06% | 8.77 | No |
| ITC.NS | 280.7 | 15 | No | No | No | -0.61% | 2.43 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.