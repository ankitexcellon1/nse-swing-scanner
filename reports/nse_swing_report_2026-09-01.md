# NSE Swing Scanner Report

Report date: 2026-09-01
Run time: 2026-09-01 00:58 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24175.65
- Nifty return: 0.35%
- Nifty EMA20: 24260.09
- Nifty EMA50: 24192.98
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 3
- Passed momentum filter: 1
- Passed volume filter: 0
- Passed relative strength filter: 7
- Passed risk-reward filter: 5
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Larsen & Toubro (LT.NS)
- Score: 50/100
- Close: 4045.8
- Setup type: Trend watchlist / below resistance
- RSI14: 45.66
- Volume vs AvgVol20: 893956 vs 1396456
- Relative strength vs Nifty: 0.12%
- Nearest support: 3923.2
- Nearest resistance: 4125.3
- Stop-loss: 3970.01
- Target 1: 4125.3
- Risk-reward: 1.05

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

### Tata Consultancy Services (TCS.NS)
- Score: 40/100
- Close: 2342.0
- Setup type: Trend watchlist / below resistance
- RSI14: 40.26
- Volume vs AvgVol20: 4054069 vs 2743140
- Relative strength vs Nifty: 3.81%
- Nearest support: 2243.9
- Nearest resistance: 2473.7
- Stop-loss: 2259.76
- Target 1: 2473.7
- Risk-reward: 1.6

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

### Infosys (INFY.NS)
- Score: 40/100
- Close: 1144.0
- Setup type: Trend watchlist / below resistance
- RSI14: 40.09
- Volume vs AvgVol20: 9621969 vs 8016826
- Relative strength vs Nifty: 2.64%
- Nearest support: 1107.2
- Nearest resistance: 1195.0
- Stop-loss: 1108.29
- Target 1: 1195.0
- Risk-reward: 1.43

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
- State Bank of India (SBIN.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Bharti Airtel (BHARTIARTL.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ICICI Bank (ICICIBANK.NS): Score 10/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| LT.NS | 4045.8 | 50 | Yes | No | No | 0.12% | 1.05 | No |
| TCS.NS | 2342.0 | 40 | Yes | No | No | 3.81% | 1.6 | No |
| INFY.NS | 1144.0 | 40 | Yes | No | No | 2.64% | 1.43 | No |
| SBIN.NS | 1047.5 | 40 | No | No | No | 0.09% | 3.63 | No |
| AXISBANK.NS | 1265.0 | 40 | No | Yes | No | 0.37% | 0.25 | No |
| RELIANCE.NS | 1287.0 | 30 | No | No | No | 0.02% | 2.96 | No |
| HDFCBANK.NS | 720.3 | 30 | No | No | No | 0.96% | 3.62 | No |
| BHARTIARTL.NS | 1882.4 | 15 | No | No | No | -0.13% | 36.24 | No |
| ITC.NS | 266.0 | 15 | No | No | No | -1.47% | 26.55 | No |
| ICICIBANK.NS | 1422.8 | 10 | No | No | No | -1.75% | 1.35 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.