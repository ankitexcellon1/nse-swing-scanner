# NSE Swing Scanner Report

Report date: 2026-08-13
Run time: 2026-08-13 19:56 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24395.85
- Nifty return: -0.16%
- Nifty EMA20: 24363.31
- Nifty EMA50: 24181.26
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 5
- Passed momentum filter: 3
- Passed volume filter: 1
- Passed relative strength filter: 5
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Bharti Airtel (BHARTIARTL.NS)
- Score: 70/100
- Close: 1939.1
- Setup type: Trend watchlist / below resistance
- RSI14: 59.61
- Volume vs AvgVol20: 13016341 vs 6451742
- Relative strength vs Nifty: -0.14%
- Nearest support: 1878.0
- Nearest resistance: 2031.0
- Stop-loss: 1884.76
- Target 1: 2031.0
- Risk-reward: 1.69

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: Yes
- Relative strength pass: No
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Relative strength failed: stock did not outperform Nifty.
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Relative strength concern: the stock is not clearly outperforming Nifty.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Tata Consultancy Services (TCS.NS)
- Score: 55/100
- Close: 2375.0
- Setup type: Trend watchlist / below resistance
- RSI14: 58.27
- Volume vs AvgVol20: 2119174 vs 3764224
- Relative strength vs Nifty: 1.24%
- Nearest support: 2187.8
- Nearest resistance: 2495.0
- Stop-loss: 2261.78
- Target 1: 2495.0
- Risk-reward: 1.06

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
- Close: 1083.0
- Setup type: Trend watchlist / below resistance
- RSI14: 72.7
- Volume vs AvgVol20: 9501882 vs 11434984
- Relative strength vs Nifty: 0.25%
- Nearest support: 1000.8
- Nearest resistance: 1124.5
- Stop-loss: 1051.86
- Target 1: 1124.5
- Risk-reward: 1.33

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
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Rejected Stocks
- Infosys (INFY.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ICICI Bank (ICICIBANK.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| BHARTIARTL.NS | 1939.1 | 70 | Yes | Yes | Yes | -0.14% | 1.69 | No |
| TCS.NS | 2375.0 | 55 | Yes | Yes | No | 1.24% | 1.06 | No |
| SBIN.NS | 1083.0 | 50 | Yes | No | No | 0.25% | 1.33 | No |
| INFY.NS | 1175.0 | 40 | Yes | No | No | 0.07% | 0.42 | No |
| LT.NS | 4070.7 | 40 | Yes | No | No | 1.42% | 0.1 | No |
| ITC.NS | 278.5 | 30 | No | No | No | 1.01% | 4.53 | No |
| ICICIBANK.NS | 1406.8 | 25 | No | No | No | -1.58% | 121.98 | No |
| RELIANCE.NS | 1317.0 | 15 | No | Yes | No | -0.74% | 0.94 | No |
| HDFCBANK.NS | 725.0 | 15 | No | No | No | -0.39% | 32.9 | No |
| AXISBANK.NS | 1221.8 | 15 | No | No | No | -0.51% | 9.93 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.