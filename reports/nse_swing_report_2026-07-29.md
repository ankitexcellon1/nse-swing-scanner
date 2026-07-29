# NSE Swing Scanner Report

Report date: 2026-07-29
Run time: 2026-07-29 20:42 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24250.2
- Nifty return: 1.1%
- Nifty EMA20: 24048.71
- Nifty EMA50: 23990.81
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 2
- Passed momentum filter: 3
- Passed volume filter: 1
- Passed relative strength filter: 5
- Passed risk-reward filter: 7
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 50/100
- Close: 1437.9
- Setup type: Trend watchlist / below resistance
- RSI14: 68.94
- Volume vs AvgVol20: 10855961 vs 12956502
- Relative strength vs Nifty: -0.6%
- Nearest support: 1367.7
- Nearest resistance: 1480.0
- Stop-loss: 1400.72
- Target 1: 1480.0
- Risk-reward: 1.13

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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 50/100
- Close: 1950.2
- Setup type: Trend watchlist / below resistance
- RSI14: 53.84
- Volume vs AvgVol20: 6315568 vs 5931042
- Relative strength vs Nifty: 1.44%
- Nearest support: 1845.6
- Nearest resistance: 1966.0
- Stop-loss: 1904.24
- Target 1: 1966.0
- Risk-reward: 0.34

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
- Infosys (INFY.NS): Score 65/100. Technical trend failed: price/EMA structure is not clean.
- Larsen & Toubro (LT.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- State Bank of India (SBIN.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| INFY.NS | 1155.6 | 65 | No | Yes | Yes | 3.41% | 2.0 | No |
| ICICIBANK.NS | 1437.9 | 50 | Yes | Yes | No | -0.6% | 1.13 | No |
| BHARTIARTL.NS | 1950.2 | 50 | Yes | No | No | 1.44% | 0.34 | No |
| LT.NS | 3931.4 | 40 | No | No | No | 1.49% | 2.15 | No |
| TCS.NS | 2446.6 | 30 | No | No | No | 0.93% | 2.0 | No |
| HDFCBANK.NS | 748.2 | 30 | No | No | No | 0.64% | 5.85 | No |
| SBIN.NS | 1013.7 | 25 | No | No | No | -1.05% | 4.13 | No |
| RELIANCE.NS | 1275.9 | 15 | No | No | No | -0.45% | 2.68 | No |
| ITC.NS | 286.25 | 15 | No | Yes | No | -0.54% | 0.84 | No |
| AXISBANK.NS | 1235.4 | 15 | No | No | No | -0.13% | 5.74 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.