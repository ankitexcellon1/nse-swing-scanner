# NSE Swing Scanner Report

Report date: 2026-07-14
Run time: 2026-07-14 20:26 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24052.05
- Nifty return: -0.66%
- Nifty EMA20: 24031.45
- Nifty EMA50: 23950.06
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 3
- Passed momentum filter: 5
- Passed volume filter: 1
- Passed relative strength filter: 5
- Passed risk-reward filter: 3
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 65/100
- Close: 1407.7
- Setup type: Trend watchlist / below resistance
- RSI14: 60.99
- Volume vs AvgVol20: 14132948 vs 11813460
- Relative strength vs Nifty: 0.53%
- Nearest support: 1326.3
- Nearest resistance: 1433.0
- Stop-loss: 1371.64
- Target 1: 1433.0
- Risk-reward: 0.7

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
- Close: 1936.5
- Setup type: Trend watchlist / below resistance
- RSI14: 61.14
- Volume vs AvgVol20: 6963829 vs 6710360
- Relative strength vs Nifty: 2.48%
- Nearest support: 1833.1
- Nearest resistance: 1966.0
- Stop-loss: 1882.67
- Target 1: 1966.0
- Risk-reward: 0.55

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

### HDFC Bank (HDFCBANK.NS)
- Score: 40/100
- Close: 809.4
- Setup type: Trend watchlist / below resistance
- RSI14: 58.77
- Volume vs AvgVol20: 25604027 vs 34578852
- Relative strength vs Nifty: -0.39%
- Nearest support: 772.55
- Nearest resistance: 843.0
- Stop-loss: 788.9
- Target 1: 843.0
- Risk-reward: 1.64

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
- Tata Consultancy Services (TCS.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Reliance Industries (RELIANCE.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- State Bank of India (SBIN.NS): Score 25/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1407.7 | 65 | Yes | Yes | No | 0.53% | 0.7 | No |
| BHARTIARTL.NS | 1936.5 | 65 | Yes | Yes | No | 2.48% | 0.55 | No |
| TCS.NS | 2200.6 | 50 | No | Yes | Yes | 1.54% | 0.32 | No |
| HDFCBANK.NS | 809.4 | 40 | Yes | Yes | No | -0.39% | 1.64 | No |
| AXISBANK.NS | 1317.6 | 40 | No | No | No | 0.52% | 3.25 | No |
| RELIANCE.NS | 1293.0 | 30 | No | No | No | 0.36% | 2.43 | No |
| SBIN.NS | 1015.4 | 25 | No | No | No | -1.42% | 5.55 | No |
| INFY.NS | 1092.9 | 15 | No | Yes | No | -0.22% | 1.48 | No |
| LT.NS | 3848.7 | 0 | No | No | No | -1.37% | 0 | No |
| ITC.NS | 275.55 | 0 | No | No | No | -0.81% | 0 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.