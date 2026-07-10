# NSE Swing Scanner Report

Report date: 2026-07-10
Run time: 2026-07-10 21:06 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24206.9
- Nifty return: 1.02%
- Nifty EMA20: 24010.15
- Nifty EMA50: 23935.09
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 2
- Passed volume filter: 0
- Passed relative strength filter: 6
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 65/100
- Close: 1401.2
- Setup type: Trend watchlist / below resistance
- RSI14: 62.55
- Volume vs AvgVol20: 6409422 vs 12064334
- Relative strength vs Nifty: 0.46%
- Nearest support: 1318.7
- Nearest resistance: 1433.0
- Stop-loss: 1361.88
- Target 1: 1433.0
- Risk-reward: 0.81

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
- Close: 1036.0
- Setup type: Trend watchlist / below resistance
- RSI14: 48.25
- Volume vs AvgVol20: 8789466 vs 10232444
- Relative strength vs Nifty: 0.34%
- Nearest support: 1004.35
- Nearest resistance: 1059.8
- Stop-loss: 1008.44
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

### HDFC Bank (HDFCBANK.NS)
- Score: 40/100
- Close: 824.95
- Setup type: Trend watchlist / below resistance
- RSI14: 67.99
- Volume vs AvgVol20: 23592799 vs 35601980
- Relative strength vs Nifty: -0.11%
- Nearest support: 753.1
- Nearest resistance: 843.0
- Stop-loss: 802.82
- Target 1: 843.0
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
- Larsen & Toubro (LT.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Bharti Airtel (BHARTIARTL.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Tata Consultancy Services (TCS.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1401.2 | 65 | Yes | Yes | No | 0.46% | 0.81 | No |
| SBIN.NS | 1036.0 | 50 | Yes | No | No | 0.34% | 0.86 | No |
| HDFCBANK.NS | 824.95 | 40 | Yes | Yes | No | -0.11% | 0.82 | No |
| LT.NS | 3945.8 | 40 | No | No | No | 0.52% | 4.19 | No |
| AXISBANK.NS | 1323.7 | 40 | No | No | No | 0.99% | 2.43 | No |
| BHARTIARTL.NS | 1920.4 | 35 | Yes | No | No | -1.57% | 0.88 | No |
| INFY.NS | 1068.0 | 30 | No | No | No | 0.62% | 2.04 | No |
| RELIANCE.NS | 1307.8 | 15 | No | No | No | 1.17% | 1.18 | No |
| ITC.NS | 281.75 | 15 | No | No | No | -1.13% | 7.31 | No |
| TCS.NS | 2069.0 | 0 | No | No | No | -0.07% | 1.8 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.