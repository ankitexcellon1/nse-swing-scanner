# NSE Swing Scanner Report

Report date: 2026-07-16
Run time: 2026-07-16 20:36 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24072.75
- Nifty return: -0.02%
- Nifty EMA20: 24039.44
- Nifty EMA50: 23959.72
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 5
- Passed volume filter: 0
- Passed relative strength filter: 7
- Passed risk-reward filter: 2
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 65/100
- Close: 1418.2
- Setup type: Trend watchlist / below resistance
- RSI14: 60.12
- Volume vs AvgVol20: 10164952 vs 11895073
- Relative strength vs Nifty: 0.16%
- Nearest support: 1331.4
- Nearest resistance: 1433.0
- Stop-loss: 1381.34
- Target 1: 1433.0
- Risk-reward: 0.4

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
- Score: 65/100
- Close: 1921.8
- Setup type: Trend watchlist / below resistance
- RSI14: 63.64
- Volume vs AvgVol20: 4644234 vs 6634907
- Relative strength vs Nifty: 0.2%
- Nearest support: 1833.1
- Nearest resistance: 1966.0
- Stop-loss: 1866.35
- Target 1: 1966.0
- Risk-reward: 0.8

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
- Close: 1031.2
- Setup type: Trend watchlist / below resistance
- RSI14: 44.79
- Volume vs AvgVol20: 7705499 vs 10259055
- Relative strength vs Nifty: 0.13%
- Nearest support: 1011.4
- Nearest resistance: 1059.8
- Stop-loss: 1011.4
- Target 1: 1059.8
- Risk-reward: 1.44

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

### HDFC Bank (HDFCBANK.NS)
- Score: 40/100
- Close: 808.3
- Setup type: Trend watchlist / below resistance
- RSI14: 55.85
- Volume vs AvgVol20: 18694378 vs 32893192
- Relative strength vs Nifty: -0.86%
- Nearest support: 772.55
- Nearest resistance: 843.0
- Stop-loss: 786.67
- Target 1: 843.0
- Risk-reward: 1.6

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
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1418.2 | 65 | Yes | Yes | No | 0.16% | 0.4 | No |
| BHARTIARTL.NS | 1921.8 | 65 | Yes | Yes | No | 0.2% | 0.8 | No |
| SBIN.NS | 1031.2 | 50 | Yes | No | No | 0.13% | 1.44 | No |
| HDFCBANK.NS | 808.3 | 40 | Yes | Yes | No | -0.86% | 1.6 | No |
| TCS.NS | 2201.0 | 30 | No | Yes | No | 0.56% | 0.27 | No |
| INFY.NS | 1082.4 | 30 | No | Yes | No | 0.59% | 1.25 | No |
| ITC.NS | 279.35 | 30 | No | No | No | 1.0% | 3.49 | No |
| AXISBANK.NS | 1307.6 | 25 | No | No | No | -0.34% | 6.01 | No |
| RELIANCE.NS | 1296.6 | 15 | No | No | No | 0.1% | 1.93 | No |
| LT.NS | 3775.6 | 0 | No | No | No | -0.2% | 0 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.