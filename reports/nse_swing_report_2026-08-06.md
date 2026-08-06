# NSE Swing Scanner Report

Report date: 2026-08-06
Run time: 2026-08-06 20:50 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24636.0
- Nifty return: 0.05%
- Nifty EMA20: 24286.46
- Nifty EMA50: 24113.42
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 6
- Passed volume filter: 1
- Passed relative strength filter: 5
- Passed risk-reward filter: 3
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### State Bank of India (SBIN.NS)
- Score: 80/100
- Close: 1085.0
- Setup type: Breakout / momentum continuation
- RSI14: 63.14
- Volume vs AvgVol20: 13817526 vs 10013338
- Relative strength vs Nifty: 2.79%
- Nearest support: 1000.8
- Nearest resistance: 1067.0
- Stop-loss: 1056.63
- Target 1: 1141.74
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

### ICICI Bank (ICICIBANK.NS)
- Score: 65/100
- Close: 1457.5
- Setup type: Trend watchlist / below resistance
- RSI14: 55.03
- Volume vs AvgVol20: 14648895 vs 12319372
- Relative strength vs Nifty: 0.46%
- Nearest support: 1377.3
- Nearest resistance: 1480.0
- Stop-loss: 1423.25
- Target 1: 1480.0
- Risk-reward: 0.66

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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 50/100
- Close: 1948.0
- Setup type: Trend watchlist / below resistance
- RSI14: 59.26
- Volume vs AvgVol20: 5325588 vs 6162355
- Relative strength vs Nifty: -1.57%
- Nearest support: 1878.0
- Nearest resistance: 2031.0
- Stop-loss: 1894.95
- Target 1: 2031.0
- Risk-reward: 1.56

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
- Close: 2373.0
- Setup type: Trend watchlist / below resistance
- RSI14: 58.83
- Volume vs AvgVol20: 2727969 vs 4851246
- Relative strength vs Nifty: -1.71%
- Nearest support: 2016.0
- Nearest resistance: 2495.0
- Stop-loss: 2273.96
- Target 1: 2495.0
- Risk-reward: 1.23

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
- Reliance Industries (RELIANCE.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| SBIN.NS | 1085.0 | 80 | Yes | Yes | No | 2.79% | 2.0 | No |
| ICICIBANK.NS | 1457.5 | 65 | Yes | Yes | No | 0.46% | 0.66 | No |
| BHARTIARTL.NS | 1948.0 | 50 | Yes | Yes | No | -1.57% | 1.56 | No |
| TCS.NS | 2373.0 | 40 | Yes | Yes | No | -1.71% | 1.23 | No |
| RELIANCE.NS | 1325.0 | 35 | No | No | Yes | 3.47% | 0.59 | No |
| AXISBANK.NS | 1256.0 | 30 | No | No | No | 0.12% | 2.43 | No |
| INFY.NS | 1165.0 | 15 | No | Yes | No | -0.82% | 0.45 | No |
| HDFCBANK.NS | 734.3 | 15 | No | No | No | -0.15% | 40.61 | No |
| LT.NS | 4061.8 | 15 | No | No | No | 0.07% | 0.13 | No |
| ITC.NS | 285.9 | 15 | No | Yes | No | -0.42% | 0.87 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.