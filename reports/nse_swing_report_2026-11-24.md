# NSE Swing Scanner Report

Report date: 2026-11-24
Run time: 2026-11-24 06:21 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 25800.6
- Nifty return: 1.12%
- Nifty EMA20: 24569.11
- Nifty EMA50: 23951.0
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 8
- Passed momentum filter: 0
- Passed volume filter: 2
- Passed relative strength filter: 4
- Passed risk-reward filter: 6
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### HDFC Bank (HDFCBANK.NS)
- Score: 75/100
- Close: 846.0
- Setup type: Breakout / momentum continuation
- RSI14: 91.07
- Volume vs AvgVol20: 70110384 vs 38947033
- Relative strength vs Nifty: 1.82%
- Nearest support: 669.2
- Nearest resistance: 822.0
- Stop-loss: 816.32
- Target 1: 905.36
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: No
- Risk-reward pass: Yes

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Overextension risk: price is too far from EMA20 or RSI is too high.

IQ200 Red-Team Review:
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Overextension concern: entry may be late; wait for pullback or fresh confirmation.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Axis Bank (AXISBANK.NS)
- Score: 75/100
- Close: 1446.0
- Setup type: Breakout / momentum continuation
- RSI14: 86.63
- Volume vs AvgVol20: 21477017 vs 7225918
- Relative strength vs Nifty: 3.6%
- Nearest support: 1196.9
- Nearest resistance: 1380.8
- Stop-loss: 1395.7
- Target 1: 1546.61
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: No
- Risk-reward pass: Yes

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Overextension risk: price is too far from EMA20 or RSI is too high.

IQ200 Red-Team Review:
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Overextension concern: entry may be late; wait for pullback or fresh confirmation.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### ICICI Bank (ICICIBANK.NS)
- Score: 55/100
- Close: 1640.0
- Setup type: Breakout / momentum continuation
- RSI14: 88.83
- Volume vs AvgVol20: 17973342 vs 16646996
- Relative strength vs Nifty: 0.81%
- Nearest support: 1361.4
- Nearest resistance: 1616.0
- Stop-loss: 1585.91
- Target 1: 1748.17
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: No
- Relative strength pass: Yes
- Not overextended: No
- Risk-reward pass: Yes

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Volume failed: volume is not above 1.5x 20-day average volume.
- Overextension risk: price is too far from EMA20 or RSI is too high.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Overextension concern: entry may be late; wait for pullback or fresh confirmation.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Rejected Stocks
- State Bank of India (SBIN.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Reliance Industries (RELIANCE.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Bharti Airtel (BHARTIARTL.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| HDFCBANK.NS | 846.0 | 75 | Yes | No | Yes | 1.82% | 2.0 | No |
| AXISBANK.NS | 1446.0 | 75 | Yes | No | Yes | 3.6% | 2.0 | No |
| ICICIBANK.NS | 1640.0 | 55 | Yes | No | No | 0.81% | 2.0 | No |
| SBIN.NS | 1165.1 | 40 | Yes | No | No | -0.33% | 2.0 | No |
| TCS.NS | 2376.2 | 30 | No | No | No | 0.31% | 5.13 | No |
| RELIANCE.NS | 1377.5 | 25 | Yes | No | No | -0.98% | 0.1 | No |
| LT.NS | 4209.1 | 25 | Yes | No | No | -1.17% | 0.42 | No |
| BHARTIARTL.NS | 2161.7 | 25 | Yes | No | No | -0.29% | 0.16 | No |
| ITC.NS | 299.1 | 25 | Yes | No | No | -1.75% | 0.26 | No |
| INFY.NS | 1098.0 | 15 | No | No | No | -0.56% | 2.17 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.