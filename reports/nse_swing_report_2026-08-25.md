# NSE Swing Scanner Report

Report date: 2026-08-25
Run time: 2026-08-25 19:24 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24334.55
- Nifty return: 0.48%
- Nifty EMA20: 24296.14
- Nifty EMA50: 24197.5
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 2
- Passed volume filter: 0
- Passed relative strength filter: 8
- Passed risk-reward filter: 5
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Larsen & Toubro (LT.NS)
- Score: 80/100
- Close: 4119.0
- Setup type: Breakout / momentum continuation
- RSI14: 67.03
- Volume vs AvgVol20: 1313304 vs 1591483
- Relative strength vs Nifty: 0.16%
- Nearest support: 3793.0
- Nearest resistance: 4100.0
- Stop-loss: 4043.64
- Target 1: 4269.73
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
- Close: 1422.7
- Setup type: Trend watchlist / below resistance
- RSI14: 40.2
- Volume vs AvgVol20: 7973577 vs 9672223
- Relative strength vs Nifty: 0.06%
- Nearest support: 1391.5
- Nearest resistance: 1460.0
- Stop-loss: 1394.56
- Target 1: 1460.0
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
- Momentum caution: RSI is not strong enough for a clean swing setup.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Bharti Airtel (BHARTIARTL.NS)
- Score: 50/100
- Close: 1947.0
- Setup type: Trend watchlist / below resistance
- RSI14: 44.7
- Volume vs AvgVol20: 3820190 vs 6444272
- Relative strength vs Nifty: 0.14%
- Nearest support: 1892.4
- Nearest resistance: 2031.0
- Stop-loss: 1899.33
- Target 1: 2031.0
- Risk-reward: 1.76

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
- RSI14: 40.47
- Volume vs AvgVol20: 8066504 vs 10439974
- Relative strength vs Nifty: 0.76%
- Nearest support: 1097.0
- Nearest resistance: 1195.0
- Stop-loss: 1109.71
- Target 1: 1195.0
- Risk-reward: 1.49

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
- Reliance Industries (RELIANCE.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ITC (ITC.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| LT.NS | 4119.0 | 80 | Yes | Yes | No | 0.16% | 2.0 | No |
| ICICIBANK.NS | 1422.7 | 50 | Yes | No | No | 0.06% | 1.33 | No |
| BHARTIARTL.NS | 1947.0 | 50 | Yes | No | No | 0.14% | 1.76 | No |
| INFY.NS | 1144.0 | 40 | Yes | No | No | 0.76% | 1.49 | No |
| SBIN.NS | 1048.0 | 40 | No | No | No | 0.34% | 2.46 | No |
| RELIANCE.NS | 1317.0 | 30 | No | Yes | No | 0.07% | 0.71 | No |
| TCS.NS | 2296.2 | 30 | No | No | No | 0.05% | 5.25 | No |
| ITC.NS | 271.4 | 30 | No | No | No | 0.15% | 3.6 | No |
| HDFCBANK.NS | 727.5 | 15 | No | No | No | -0.69% | 2.71 | No |
| AXISBANK.NS | 1235.0 | 0 | No | No | No | -0.56% | 1.41 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.