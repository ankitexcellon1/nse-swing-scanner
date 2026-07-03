# NSE Swing Scanner Report

Report date: 2026-07-03
Run time: 2026-07-03 20:46 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24270.85
- Nifty return: 0.39%
- Nifty EMA20: 23913.02
- Nifty EMA50: 23883.24
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 4
- Passed volume filter: 0
- Passed relative strength filter: 5
- Passed risk-reward filter: 3
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### HDFC Bank (HDFCBANK.NS)
- Score: 55/100
- Close: 801.05
- Setup type: Trend watchlist / below resistance
- RSI14: 62.94
- Volume vs AvgVol20: 25867219 vs 33112458
- Relative strength vs Nifty: 0.26%
- Nearest support: 732.3
- Nearest resistance: 806.1
- Stop-loss: 781.73
- Target 1: 806.1
- Risk-reward: 0.26

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
- Close: 1411.4
- Setup type: Breakout / momentum continuation
- RSI14: 80.63
- Volume vs AvgVol20: 12899919 vs 14783793
- Relative strength vs Nifty: 0.42%
- Nearest support: 1243.1
- Nearest resistance: 1405.0
- Stop-loss: 1378.91
- Target 1: 1476.37
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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 55/100
- Close: 1910.4
- Setup type: Trend watchlist / below resistance
- RSI14: 65.59
- Volume vs AvgVol20: 5086693 vs 6700809
- Relative strength vs Nifty: 1.5%
- Nearest support: 1768.6
- Nearest resistance: 1927.7
- Stop-loss: 1865.82
- Target 1: 1927.7
- Risk-reward: 0.39

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
- Close: 1040.0
- Setup type: Trend watchlist / below resistance
- RSI14: 56.9
- Volume vs AvgVol20: 10438892 vs 11662706
- Relative strength vs Nifty: -1.49%
- Nearest support: 965.15
- Nearest resistance: 1059.8
- Stop-loss: 1014.07
- Target 1: 1059.8
- Risk-reward: 0.76

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
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Larsen & Toubro (LT.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Tata Consultancy Services (TCS.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 10/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| HDFCBANK.NS | 801.05 | 55 | Yes | Yes | No | 0.26% | 0.26 | No |
| ICICIBANK.NS | 1411.4 | 55 | Yes | No | No | 0.42% | 2.0 | No |
| BHARTIARTL.NS | 1910.4 | 55 | Yes | Yes | No | 1.5% | 0.39 | No |
| SBIN.NS | 1040.0 | 50 | Yes | Yes | No | -1.49% | 0.76 | No |
| INFY.NS | 1047.2 | 30 | No | No | No | 0.22% | 3.36 | No |
| LT.NS | 4026.6 | 25 | No | No | No | -1.2% | 2.58 | No |
| TCS.NS | 2093.5 | 15 | No | No | No | 0.84% | 2.0 | No |
| ITC.NS | 289.95 | 15 | No | Yes | No | -0.37% | 0.89 | No |
| AXISBANK.NS | 1342.1 | 10 | No | No | No | -1.89% | 1.73 | No |
| RELIANCE.NS | 1304.0 | 0 | No | No | No | -0.35% | 1.38 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.