# NSE Swing Scanner Report

Report date: 2026-08-17
Run time: 2026-08-17 19:12 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24287.65
- Nifty return: -0.32%
- Nifty EMA20: 24356.34
- Nifty EMA50: 24192.41
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 3
- Passed momentum filter: 4
- Passed volume filter: 0
- Passed relative strength filter: 5
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Larsen & Toubro (LT.NS)
- Score: 55/100
- Close: 4086.7
- Setup type: Breakout / momentum continuation
- RSI14: 76.33
- Volume vs AvgVol20: 1066047 vs 1661318
- Relative strength vs Nifty: 1.05%
- Nearest support: 3720.0
- Nearest resistance: 4080.0
- Stop-loss: 3991.75
- Target 1: 4276.6
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
- Close: 1061.2
- Setup type: Trend watchlist / below resistance
- RSI14: 65.13
- Volume vs AvgVol20: 7033292 vs 11292299
- Relative strength vs Nifty: -0.29%
- Nearest support: 1000.8
- Nearest resistance: 1124.5
- Stop-loss: 1028.79
- Target 1: 1124.5
- Risk-reward: 1.95

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
- Close: 1969.3
- Setup type: Trend watchlist / below resistance
- RSI14: 62.14
- Volume vs AvgVol20: 5533701 vs 6691350
- Relative strength vs Nifty: -0.82%
- Nearest support: 1878.0
- Nearest resistance: 2031.0
- Stop-loss: 1909.1
- Target 1: 2031.0
- Risk-reward: 1.02

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
- ICICI Bank (ICICIBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Reliance Industries (RELIANCE.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Tata Consultancy Services (TCS.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| LT.NS | 4086.7 | 55 | Yes | No | No | 1.05% | 2.0 | No |
| SBIN.NS | 1061.2 | 50 | Yes | Yes | No | -0.29% | 1.95 | No |
| BHARTIARTL.NS | 1969.3 | 50 | Yes | Yes | No | -0.82% | 1.02 | No |
| ICICIBANK.NS | 1415.3 | 40 | No | No | No | 0.2% | 4.52 | No |
| RELIANCE.NS | 1316.0 | 30 | No | Yes | No | 0.78% | 0.92 | No |
| HDFCBANK.NS | 729.0 | 30 | No | No | No | 0.6% | 13.53 | No |
| AXISBANK.NS | 1227.3 | 30 | No | No | No | 1.13% | 5.65 | No |
| INFY.NS | 1139.9 | 15 | No | Yes | No | -2.67% | 1.15 | No |
| TCS.NS | 2313.2 | 0 | No | No | No | -1.7% | 1.73 | No |
| ITC.NS | 273.05 | 0 | No | No | No | -1.53% | 0 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.