# NSE Swing Scanner Report

Report date: 2026-08-21
Run time: 2026-08-21 19:17 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24252.0
- Nifty return: 0.08%
- Nifty EMA20: 24299.79
- Nifty EMA50: 24190.81
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 2
- Passed momentum filter: 1
- Passed volume filter: 0
- Passed relative strength filter: 6
- Passed risk-reward filter: 6
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Larsen & Toubro (LT.NS)
- Score: 80/100
- Close: 4093.0
- Setup type: Breakout / momentum continuation
- RSI14: 58.77
- Volume vs AvgVol20: 1258681 vs 1598517
- Relative strength vs Nifty: 0.21%
- Nearest support: 3720.0
- Nearest resistance: 4086.7
- Stop-loss: 4018.12
- Target 1: 4242.76
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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 50/100
- Close: 1946.0
- Setup type: Trend watchlist / below resistance
- RSI14: 45.59
- Volume vs AvgVol20: 3016210 vs 6716374
- Relative strength vs Nifty: 0.14%
- Nearest support: 1878.0
- Nearest resistance: 2031.0
- Stop-loss: 1889.8
- Target 1: 2031.0
- Risk-reward: 1.51

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

## Rejected Stocks
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ICICI Bank (ICICIBANK.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- State Bank of India (SBIN.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| LT.NS | 4093.0 | 80 | Yes | Yes | No | 0.21% | 2.0 | No |
| BHARTIARTL.NS | 1946.0 | 50 | Yes | No | No | 0.14% | 1.51 | No |
| TCS.NS | 2302.0 | 30 | No | No | No | 0.09% | 2.29 | No |
| HDFCBANK.NS | 726.95 | 30 | No | No | No | 0.18% | 2.61 | No |
| ICICIBANK.NS | 1420.0 | 25 | No | No | No | 0.49% | 1.4 | No |
| SBIN.NS | 1048.7 | 25 | No | No | No | -0.01% | 2.45 | No |
| RELIANCE.NS | 1316.0 | 15 | No | No | No | 0.13% | 0.68 | No |
| INFY.NS | 1121.0 | 15 | No | No | No | -0.88% | 2.2 | No |
| ITC.NS | 269.4 | 15 | No | No | No | -0.91% | 5.26 | No |
| AXISBANK.NS | 1245.8 | 0 | No | No | No | -0.5% | 0.94 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.