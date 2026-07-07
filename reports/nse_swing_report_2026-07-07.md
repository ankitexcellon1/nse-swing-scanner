# NSE Swing Scanner Report

Report date: 2026-07-07
Run time: 2026-07-07 21:18 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24398.7
- Nifty return: -0.13%
- Nifty EMA20: 24003.85
- Nifty EMA50: 23924.07
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 2
- Passed volume filter: 2
- Passed relative strength filter: 7
- Passed risk-reward filter: 2
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### HDFC Bank (HDFCBANK.NS)
- Score: 75/100
- Close: 829.3
- Setup type: Trend watchlist / below resistance
- RSI14: 68.97
- Volume vs AvgVol20: 57607105 vs 36148703
- Relative strength vs Nifty: 0.06%
- Nearest support: 732.3
- Nearest resistance: 831.5
- Stop-loss: 807.22
- Target 1: 831.5
- Risk-reward: 0.1

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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 65/100
- Close: 1925.8
- Setup type: Trend watchlist / below resistance
- RSI14: 62.35
- Volume vs AvgVol20: 5767286 vs 6291082
- Relative strength vs Nifty: 0.14%
- Nearest support: 1768.6
- Nearest resistance: 1932.7
- Stop-loss: 1880.86
- Target 1: 1932.7
- Risk-reward: 0.15

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
- Close: 1038.1
- Setup type: Trend watchlist / below resistance
- RSI14: 54.65
- Volume vs AvgVol20: 11052201 vs 10901603
- Relative strength vs Nifty: 0.17%
- Nearest support: 983.0
- Nearest resistance: 1059.8
- Stop-loss: 1013.01
- Target 1: 1059.8
- Risk-reward: 0.86

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
- ITC (ITC.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ICICI Bank (ICICIBANK.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Tata Consultancy Services (TCS.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| HDFCBANK.NS | 829.3 | 75 | Yes | Yes | Yes | 0.06% | 0.1 | No |
| BHARTIARTL.NS | 1925.8 | 65 | Yes | Yes | No | 0.14% | 0.15 | No |
| SBIN.NS | 1038.1 | 50 | Yes | No | No | 0.17% | 0.86 | No |
| ITC.NS | 288.75 | 35 | No | No | Yes | 0.3% | 1.13 | No |
| INFY.NS | 1071.8 | 30 | No | No | No | 2.97% | 2.24 | No |
| ICICIBANK.NS | 1414.7 | 25 | Yes | No | No | -0.73% | 0.49 | No |
| LT.NS | 3991.9 | 25 | No | No | No | -1.09% | 2.89 | No |
| AXISBANK.NS | 1341.0 | 25 | No | No | No | 0.23% | 1.67 | No |
| TCS.NS | 2096.1 | 15 | No | No | No | 2.0% | 1.45 | No |
| RELIANCE.NS | 1308.4 | 0 | No | No | No | -0.85% | 1.2 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.