# NSE Swing Scanner Report

Report date: 2026-07-06
Run time: 2026-07-06 21:57 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24430.35
- Nifty return: 0.66%
- Nifty EMA20: 23962.29
- Nifty EMA50: 23904.7
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 3
- Passed volume filter: 2
- Passed relative strength filter: 4
- Passed risk-reward filter: 5
- Final qualified candidates: 1

## Executive Summary
1 stock(s) passed all MVP technical filters. These are research candidates only and still require manual chart, delivery, news, and event-risk confirmation.

## Final Qualified Candidates

### HDFC Bank (HDFCBANK.NS)
- Setup type: Breakout / momentum continuation
- Close: 829.85
- Buy zone: Near 829.85 only after price confirmation
- Stop-loss: 808.38
- Target 1: 872.79
- Risk-reward: 2.0
- Score: 90/100

Evidence:
- EMA20: 789.43, EMA50: 786.05, EMA200: 862.25
- RSI14: 69.92
- Volume: 63200856, AvgVol20: 35195203
- Relative strength vs Nifty: 2.94%

IQ200 Red-Team Review:
- No major technical objection found in MVP filters, but manual chart/news confirmation is still required.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Watchlist / Manual Review Only

### Bharti Airtel (BHARTIARTL.NS)
- Score: 65/100
- Close: 1925.7
- Setup type: Trend watchlist / below resistance
- RSI14: 66.12
- Volume vs AvgVol20: 2740212 vs 6521591
- Relative strength vs Nifty: 0.14%
- Nearest support: 1768.6
- Nearest resistance: 1927.7
- Stop-loss: 1881.09
- Target 1: 1927.7
- Risk-reward: 0.04

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
- Score: 55/100
- Close: 1426.9
- Setup type: Breakout / momentum continuation
- RSI14: 81.8
- Volume vs AvgVol20: 12306363 vs 14863495
- Relative strength vs Nifty: 0.44%
- Nearest support: 1243.1
- Nearest resistance: 1420.0
- Stop-loss: 1393.43
- Target 1: 1493.84
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

### State Bank of India (SBIN.NS)
- Score: 50/100
- Close: 1037.7
- Setup type: Trend watchlist / below resistance
- RSI14: 58.27
- Volume vs AvgVol20: 8759103 vs 11456021
- Relative strength vs Nifty: -0.88%
- Nearest support: 965.15
- Nearest resistance: 1059.8
- Stop-loss: 1012.55
- Target 1: 1059.8
- Risk-reward: 0.88

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
- Larsen & Toubro (LT.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 20/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Tata Consultancy Services (TCS.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 10/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| HDFCBANK.NS | 829.85 | 90 | Yes | Yes | Yes | 2.94% | 2.0 | Yes |
| BHARTIARTL.NS | 1925.7 | 65 | Yes | Yes | No | 0.14% | 0.04 | No |
| ICICIBANK.NS | 1426.9 | 55 | Yes | No | No | 0.44% | 2.0 | No |
| SBIN.NS | 1037.7 | 50 | Yes | Yes | No | -0.88% | 0.88 | No |
| LT.NS | 4041.0 | 25 | No | No | No | -0.3% | 2.46 | No |
| ITC.NS | 288.25 | 20 | No | No | Yes | -1.25% | 1.27 | No |
| RELIANCE.NS | 1321.3 | 15 | No | No | No | 0.67% | 0.8 | No |
| TCS.NS | 2057.6 | 15 | No | No | No | -2.37% | 2.15 | No |
| INFY.NS | 1042.2 | 15 | No | No | No | -1.14% | 3.09 | No |
| AXISBANK.NS | 1339.6 | 10 | No | No | No | -0.85% | 1.74 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.