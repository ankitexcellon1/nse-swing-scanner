# NSE Swing Scanner Report

Report date: 2026-11-26
Run time: 2026-11-26 03:54 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 25349.65
- Nifty return: -1.75%
- Nifty EMA20: 24643.44
- Nifty EMA50: 24005.85
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 9
- Passed momentum filter: 2
- Passed volume filter: 1
- Passed relative strength filter: 4
- Passed risk-reward filter: 1
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Tata Consultancy Services (TCS.NS)
- Score: 70/100
- Close: 2460.0
- Setup type: Trend watchlist / below resistance
- RSI14: 44.85
- Volume vs AvgVol20: 7386320 vs 3510112
- Relative strength vs Nifty: 5.28%
- Nearest support: 2317.0
- Nearest resistance: 2625.0
- Stop-loss: 2359.05
- Target 1: 2625.0
- Risk-reward: 1.63

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Momentum caution: RSI is not strong enough for a clean swing setup.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Bharti Airtel (BHARTIARTL.NS)
- Score: 65/100
- Close: 2128.5
- Setup type: Trend watchlist / below resistance
- RSI14: 68.96
- Volume vs AvgVol20: 5700272 vs 8726296
- Relative strength vs Nifty: 0.21%
- Nearest support: 1860.7
- Nearest resistance: 2172.3
- Stop-loss: 2059.3
- Target 1: 2172.3
- Risk-reward: 0.63

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

### Larsen & Toubro (LT.NS)
- Score: 50/100
- Close: 4099.9
- Setup type: Trend watchlist / below resistance
- RSI14: 64.99
- Volume vs AvgVol20: 1259578 vs 2303979
- Relative strength vs Nifty: -0.84%
- Nearest support: 3596.8
- Nearest resistance: 4259.0
- Stop-loss: 3975.31
- Target 1: 4259.0
- Risk-reward: 1.28

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
- ITC (ITC.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- HDFC Bank (HDFCBANK.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ICICI Bank (ICICIBANK.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- State Bank of India (SBIN.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| TCS.NS | 2460.0 | 70 | Yes | No | Yes | 5.28% | 1.63 | No |
| BHARTIARTL.NS | 2128.5 | 65 | Yes | Yes | No | 0.21% | 0.63 | No |
| LT.NS | 4099.9 | 50 | Yes | Yes | No | -0.84% | 1.28 | No |
| ITC.NS | 301.0 | 40 | Yes | No | No | 2.39% | 0.08 | No |
| RELIANCE.NS | 1351.0 | 35 | Yes | No | No | -0.17% | 0.83 | No |
| AXISBANK.NS | 1388.6 | 35 | Yes | No | No | -2.22% | 1.1 | No |
| INFY.NS | 1103.4 | 30 | No | No | No | 2.24% | 2.1 | No |
| HDFCBANK.NS | 817.8 | 25 | Yes | No | No | -1.58% | 0.98 | No |
| ICICIBANK.NS | 1585.5 | 25 | Yes | No | No | -1.57% | 1.03 | No |
| SBIN.NS | 1132.65 | 25 | Yes | No | No | -1.04% | 0.92 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.