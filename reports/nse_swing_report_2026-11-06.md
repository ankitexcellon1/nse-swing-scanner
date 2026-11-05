# NSE Swing Scanner Report

Report date: 2026-11-06
Run time: 2026-11-06 02:31 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 23960.6
- Nifty return: 0.63%
- Nifty EMA20: 23081.52
- Nifty EMA50: 23225.79
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 4
- Passed volume filter: 2
- Passed relative strength filter: 3
- Passed risk-reward filter: 3
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Tata Consultancy Services (TCS.NS)
- Score: 40/100
- Close: 2436.0
- Setup type: Trend watchlist / below resistance
- RSI14: 64.05
- Volume vs AvgVol20: 3142051 vs 5894677
- Relative strength vs Nifty: -3.15%
- Nearest support: 2060.0
- Nearest resistance: 2625.0
- Stop-loss: 2325.69
- Target 1: 2625.0
- Risk-reward: 1.71

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

### Infosys (INFY.NS)
- Score: 40/100
- Close: 1128.2
- Setup type: Trend watchlist / below resistance
- RSI14: 56.09
- Volume vs AvgVol20: 9333345 vs 16689602
- Relative strength vs Nifty: -2.36%
- Nearest support: 990.1
- Nearest resistance: 1197.8
- Stop-loss: 1054.57
- Target 1: 1197.8
- Risk-reward: 0.95

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
- HDFC Bank (HDFCBANK.NS): Score 65/100. Technical trend failed: price/EMA structure is not clean.
- ITC (ITC.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Overextension risk: price is too far from EMA20 or RSI is too high.
- ICICI Bank (ICICIBANK.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- State Bank of India (SBIN.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Bharti Airtel (BHARTIARTL.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| HDFCBANK.NS | 736.7 | 65 | No | Yes | Yes | 0.91% | 2.0 | No |
| ITC.NS | 280.0 | 50 | No | No | Yes | 1.6% | 2.0 | No |
| TCS.NS | 2436.0 | 40 | Yes | Yes | No | -3.15% | 1.71 | No |
| INFY.NS | 1128.2 | 40 | Yes | Yes | No | -2.36% | 0.95 | No |
| ICICIBANK.NS | 1424.1 | 35 | Yes | No | No | -0.66% | 0.17 | No |
| SBIN.NS | 979.0 | 30 | No | Yes | No | 0.27% | 0.88 | No |
| BHARTIARTL.NS | 2067.6 | 25 | Yes | No | No | -0.5% | 0.18 | No |
| RELIANCE.NS | 1311.0 | 15 | No | No | No | -0.39% | 2.0 | No |
| LT.NS | 3944.4 | 0 | No | No | No | -0.73% | 0.16 | No |
| AXISBANK.NS | 1232.0 | 0 | No | No | No | -0.69% | 1.76 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.