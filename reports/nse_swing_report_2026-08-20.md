# NSE Swing Scanner Report

Report date: 2026-08-20
Run time: 2026-08-20 19:19 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24231.85
- Nifty return: 0.64%
- Nifty EMA20: 24297.48
- Nifty EMA50: 24176.16
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 2
- Passed momentum filter: 3
- Passed volume filter: 1
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
- Score: 65/100
- Close: 4081.0
- Setup type: Trend watchlist / below resistance
- RSI14: 65.38
- Volume vs AvgVol20: 1056002 vs 1635284
- Relative strength vs Nifty: 0.34%
- Nearest support: 3720.0
- Nearest resistance: 4086.7
- Stop-loss: 4001.03
- Target 1: 4086.7
- Risk-reward: 0.07

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
- Close: 1941.7
- Setup type: Trend watchlist / below resistance
- RSI14: 44.49
- Volume vs AvgVol20: 4388969 vs 6789662
- Relative strength vs Nifty: 0.38%
- Nearest support: 1878.0
- Nearest resistance: 2031.0
- Stop-loss: 1882.29
- Target 1: 2031.0
- Risk-reward: 1.5

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
- ITC (ITC.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.
- ICICI Bank (ICICIBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- State Bank of India (SBIN.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Tata Consultancy Services (TCS.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| LT.NS | 4081.0 | 65 | Yes | Yes | No | 0.34% | 0.07 | No |
| BHARTIARTL.NS | 1941.7 | 50 | Yes | No | No | 0.38% | 1.5 | No |
| ITC.NS | 271.65 | 50 | No | No | Yes | 1.08% | 3.6 | No |
| ICICIBANK.NS | 1411.9 | 40 | No | No | No | 0.07% | 2.36 | No |
| SBIN.NS | 1048.0 | 40 | No | Yes | No | -0.7% | 2.4 | No |
| HDFCBANK.NS | 725.05 | 30 | No | No | No | 0.06% | 3.3 | No |
| AXISBANK.NS | 1251.0 | 30 | No | Yes | No | 0.66% | 0.68 | No |
| TCS.NS | 2298.0 | 15 | No | No | No | -0.25% | 2.16 | No |
| INFY.NS | 1130.0 | 15 | No | No | No | 0.27% | 1.57 | No |
| RELIANCE.NS | 1313.2 | 0 | No | No | No | -0.47% | 0.76 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.