# NSE Swing Scanner Report

Report date: 2026-08-14
Run time: 2026-08-14 19:49 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24366.0
- Nifty return: -0.12%
- Nifty EMA20: 24363.57
- Nifty EMA50: 24188.51
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 5
- Passed momentum filter: 4
- Passed volume filter: 1
- Passed relative strength filter: 4
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Bharti Airtel (BHARTIARTL.NS)
- Score: 85/100
- Close: 1992.1
- Setup type: Trend watchlist / below resistance
- RSI14: 66.77
- Volume vs AvgVol20: 12282326 vs 6830222
- Relative strength vs Nifty: 2.85%
- Nearest support: 1878.0
- Nearest resistance: 2031.0
- Stop-loss: 1932.74
- Target 1: 2031.0
- Risk-reward: 0.66

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

### State Bank of India (SBIN.NS)
- Score: 50/100
- Close: 1067.7
- Setup type: Trend watchlist / below resistance
- RSI14: 64.76
- Volume vs AvgVol20: 6266769 vs 11501659
- Relative strength vs Nifty: -1.29%
- Nearest support: 1000.8
- Nearest resistance: 1124.5
- Stop-loss: 1035.58
- Target 1: 1124.5
- Risk-reward: 1.77

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

### Infosys (INFY.NS)
- Score: 40/100
- Close: 1169.2
- Setup type: Trend watchlist / below resistance
- RSI14: 69.82
- Volume vs AvgVol20: 5842970 vs 13234900
- Relative strength vs Nifty: -0.37%
- Nearest support: 1013.9
- Nearest resistance: 1195.0
- Stop-loss: 1124.37
- Target 1: 1195.0
- Risk-reward: 0.58

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
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ITC (ITC.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Tata Consultancy Services (TCS.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| BHARTIARTL.NS | 1992.1 | 85 | Yes | Yes | Yes | 2.85% | 0.66 | No |
| SBIN.NS | 1067.7 | 50 | Yes | Yes | No | -1.29% | 1.77 | No |
| INFY.NS | 1169.2 | 40 | Yes | Yes | No | -0.37% | 0.58 | No |
| ICICIBANK.NS | 1417.0 | 40 | No | No | No | 0.85% | 5.94 | No |
| HDFCBANK.NS | 727.0 | 30 | No | No | No | 0.4% | 19.34 | No |
| ITC.NS | 278.2 | 30 | No | No | No | 0.01% | 5.12 | No |
| TCS.NS | 2361.0 | 25 | Yes | No | No | -0.47% | 1.19 | No |
| LT.NS | 4057.0 | 25 | Yes | No | No | -0.22% | 0.25 | No |
| RELIANCE.NS | 1310.0 | 15 | No | Yes | No | -0.41% | 1.14 | No |
| AXISBANK.NS | 1217.4 | 15 | No | No | No | -0.24% | 17.0 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.