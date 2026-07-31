# NSE Swing Scanner Report

Report date: 2026-07-31
Run time: 2026-07-31 20:53 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24383.6
- Nifty return: 0.27%
- Nifty EMA20: 24103.73
- Nifty EMA50: 24018.5
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 4
- Passed volume filter: 0
- Passed relative strength filter: 2
- Passed risk-reward filter: 3
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Bharti Airtel (BHARTIARTL.NS)
- Score: 80/100
- Close: 1972.0
- Setup type: Breakout / momentum continuation
- RSI14: 64.55
- Volume vs AvgVol20: 6528923 vs 6006848
- Relative strength vs Nifty: 0.51%
- Nearest support: 1875.1
- Nearest resistance: 1966.0
- Stop-loss: 1926.09
- Target 1: 2063.82
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
- Score: 50/100
- Close: 1435.4
- Setup type: Trend watchlist / below resistance
- RSI14: 60.14
- Volume vs AvgVol20: 8751419 vs 12667081
- Relative strength vs Nifty: -0.17%
- Nearest support: 1375.9
- Nearest resistance: 1480.0
- Stop-loss: 1400.8
- Target 1: 1480.0
- Risk-reward: 1.29

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
- Close: 2365.6
- Setup type: Trend watchlist / below resistance
- RSI14: 68.77
- Volume vs AvgVol20: 4343039 vs 5012360
- Relative strength vs Nifty: -2.99%
- Nearest support: 2016.0
- Nearest resistance: 2495.0
- Stop-loss: 2271.0
- Target 1: 2495.0
- Risk-reward: 1.37

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
- State Bank of India (SBIN.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 10/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| BHARTIARTL.NS | 1972.0 | 80 | Yes | Yes | No | 0.51% | 2.0 | No |
| ICICIBANK.NS | 1435.4 | 50 | Yes | Yes | No | -0.17% | 1.29 | No |
| TCS.NS | 2365.6 | 40 | Yes | Yes | No | -2.99% | 1.37 | No |
| SBIN.NS | 1027.4 | 35 | Yes | No | No | -0.07% | 1.49 | No |
| RELIANCE.NS | 1307.8 | 15 | No | No | No | 0.88% | 1.18 | No |
| INFY.NS | 1130.1 | 15 | No | Yes | No | -2.43% | 1.18 | No |
| HDFCBANK.NS | 748.15 | 15 | No | No | No | -1.04% | 5.87 | No |
| AXISBANK.NS | 1229.5 | 15 | No | No | No | -0.22% | 7.59 | No |
| LT.NS | 3938.9 | 10 | No | No | No | -0.24% | 1.61 | No |
| ITC.NS | 281.0 | 0 | No | No | No | -1.69% | 1.77 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.