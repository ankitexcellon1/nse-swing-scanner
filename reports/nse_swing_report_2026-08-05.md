# NSE Swing Scanner Report

Report date: 2026-08-05
Run time: 2026-08-05 20:47 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24624.65
- Nifty return: 0.04%
- Nifty EMA20: 24249.67
- Nifty EMA50: 24092.1
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 6
- Passed volume filter: 3
- Passed relative strength filter: 4
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Bharti Airtel (BHARTIARTL.NS)
- Score: 85/100
- Close: 1978.0
- Setup type: Trend watchlist / below resistance
- RSI14: 64.44
- Volume vs AvgVol20: 14286588 vs 6453308
- Relative strength vs Nifty: 0.36%
- Nearest support: 1875.1
- Nearest resistance: 1987.4
- Stop-loss: 1926.15
- Target 1: 1987.4
- Risk-reward: 0.18

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### State Bank of India (SBIN.NS)
- Score: 65/100
- Close: 1055.0
- Setup type: Trend watchlist / below resistance
- RSI14: 58.62
- Volume vs AvgVol20: 8706372 vs 9705509
- Relative strength vs Nifty: 1.14%
- Nearest support: 1000.8
- Nearest resistance: 1067.0
- Stop-loss: 1028.33
- Target 1: 1067.0
- Risk-reward: 0.45

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

### ICICI Bank (ICICIBANK.NS)
- Score: 50/100
- Close: 1450.1
- Setup type: Trend watchlist / below resistance
- RSI14: 60.64
- Volume vs AvgVol20: 11718835 vs 12284146
- Relative strength vs Nifty: -0.35%
- Nearest support: 1375.9
- Nearest resistance: 1480.0
- Stop-loss: 1413.15
- Target 1: 1480.0
- Risk-reward: 0.81

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

### Tata Consultancy Services (TCS.NS)
- Score: 40/100
- Close: 2413.0
- Setup type: Trend watchlist / below resistance
- RSI14: 67.19
- Volume vs AvgVol20: 3013140 vs 4904359
- Relative strength vs Nifty: -1.95%
- Nearest support: 2016.0
- Nearest resistance: 2495.0
- Stop-loss: 2313.1
- Target 1: 2495.0
- Risk-reward: 0.82

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
- Reliance Industries (RELIANCE.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.
- HDFC Bank (HDFCBANK.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| BHARTIARTL.NS | 1978.0 | 85 | Yes | Yes | Yes | 0.36% | 0.18 | No |
| SBIN.NS | 1055.0 | 65 | Yes | Yes | No | 1.14% | 0.45 | No |
| ICICIBANK.NS | 1450.1 | 50 | Yes | Yes | No | -0.35% | 0.81 | No |
| TCS.NS | 2413.0 | 40 | Yes | Yes | No | -1.95% | 0.82 | No |
| RELIANCE.NS | 1280.0 | 35 | No | No | Yes | -0.88% | 2.18 | No |
| HDFCBANK.NS | 735.0 | 35 | No | No | Yes | -0.98% | 33.12 | No |
| INFY.NS | 1174.0 | 30 | No | Yes | No | 0.52% | 0.26 | No |
| LT.NS | 4057.0 | 30 | No | No | No | 1.64% | 2.0 | No |
| ITC.NS | 286.95 | 15 | No | Yes | No | -0.75% | 0.72 | No |
| AXISBANK.NS | 1253.9 | 15 | No | No | No | -0.67% | 2.37 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.