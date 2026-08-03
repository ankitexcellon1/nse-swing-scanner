# NSE Swing Scanner Report

Report date: 2026-08-03
Run time: 2026-08-03 21:16 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24774.3
- Nifty return: 1.6%
- Nifty EMA20: 24167.6
- Nifty EMA50: 24048.14
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 6
- Passed volume filter: 1
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
- Close: 1460.0
- Setup type: Trend watchlist / below resistance
- RSI14: 67.38
- Volume vs AvgVol20: 7689346 vs 12436252
- Relative strength vs Nifty: 0.11%
- Nearest support: 1375.9
- Nearest resistance: 1480.0
- Stop-loss: 1424.63
- Target 1: 1480.0
- Risk-reward: 0.57

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
- Score: 65/100
- Close: 1045.0
- Setup type: Trend watchlist / below resistance
- RSI14: 60.63
- Volume vs AvgVol20: 10488126 vs 10101778
- Relative strength vs Nifty: 0.11%
- Nearest support: 1000.8
- Nearest resistance: 1067.0
- Stop-loss: 1018.38
- Target 1: 1067.0
- Risk-reward: 0.83

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
- Close: 1970.5
- Setup type: Trend watchlist / below resistance
- RSI14: 58.17
- Volume vs AvgVol20: 4360263 vs 6087873
- Relative strength vs Nifty: -1.68%
- Nearest support: 1875.1
- Nearest resistance: 1976.4
- Stop-loss: 1925.84
- Target 1: 1976.4
- Risk-reward: 0.13

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
- Tata Consultancy Services (TCS.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ITC (ITC.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1460.0 | 65 | Yes | Yes | No | 0.11% | 0.57 | No |
| SBIN.NS | 1045.0 | 65 | Yes | Yes | No | 0.11% | 0.83 | No |
| BHARTIARTL.NS | 1970.5 | 50 | Yes | Yes | No | -1.68% | 0.13 | No |
| TCS.NS | 2473.7 | 40 | Yes | No | No | 2.97% | 0.21 | No |
| LT.NS | 4025.0 | 40 | No | Yes | No | 0.59% | 0.45 | No |
| AXISBANK.NS | 1272.0 | 40 | No | No | No | 1.86% | 2.39 | No |
| ITC.NS | 287.0 | 35 | No | No | Yes | 0.54% | 0.49 | No |
| INFY.NS | 1180.0 | 30 | No | Yes | No | 2.82% | 0.15 | No |
| RELIANCE.NS | 1319.0 | 15 | No | Yes | No | -0.74% | 0.85 | No |
| HDFCBANK.NS | 753.0 | 15 | No | No | No | -0.95% | 4.29 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.