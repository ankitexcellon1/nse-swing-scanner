# NSE Swing Scanner Report

Report date: 2026-08-04
Run time: 2026-08-04 20:58 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24614.9
- Nifty return: -0.64%
- Nifty EMA20: 24210.2
- Nifty EMA50: 24070.37
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 3
- Passed volume filter: 0
- Passed relative strength filter: 5
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
- Close: 1454.6
- Setup type: Trend watchlist / below resistance
- RSI14: 63.03
- Volume vs AvgVol20: 11380139 vs 12222920
- Relative strength vs Nifty: 0.27%
- Nearest support: 1375.9
- Nearest resistance: 1480.0
- Stop-loss: 1418.28
- Target 1: 1480.0
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
- Close: 1970.1
- Setup type: Trend watchlist / below resistance
- RSI14: 63.62
- Volume vs AvgVol20: 4946436 vs 6046870
- Relative strength vs Nifty: 0.62%
- Nearest support: 1875.1
- Nearest resistance: 1987.4
- Stop-loss: 1924.7
- Target 1: 1987.4
- Risk-reward: 0.38

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
- Close: 1042.7
- Setup type: Trend watchlist / below resistance
- RSI14: 54.97
- Volume vs AvgVol20: 8539502 vs 9977041
- Relative strength vs Nifty: 0.42%
- Nearest support: 1000.8
- Nearest resistance: 1067.0
- Stop-loss: 1016.67
- Target 1: 1067.0
- Risk-reward: 0.93

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

### Tata Consultancy Services (TCS.NS)
- Score: 40/100
- Close: 2460.0
- Setup type: Trend watchlist / below resistance
- RSI14: 73.28
- Volume vs AvgVol20: 2791949 vs 4937010
- Relative strength vs Nifty: 0.09%
- Nearest support: 2016.0
- Nearest resistance: 2495.0
- Stop-loss: 2361.1
- Target 1: 2495.0
- Risk-reward: 0.35

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
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Rejected Stocks
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 10/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1454.6 | 65 | Yes | Yes | No | 0.27% | 0.7 | No |
| BHARTIARTL.NS | 1970.1 | 65 | Yes | Yes | No | 0.62% | 0.38 | No |
| SBIN.NS | 1042.7 | 50 | Yes | No | No | 0.42% | 0.93 | No |
| TCS.NS | 2460.0 | 40 | Yes | No | No | 0.09% | 0.35 | No |
| INFY.NS | 1167.5 | 15 | No | Yes | No | -0.42% | 0.38 | No |
| HDFCBANK.NS | 742.0 | 15 | No | No | No | -0.82% | 10.1 | No |
| ITC.NS | 289.0 | 15 | No | No | No | 1.34% | 0.46 | No |
| AXISBANK.NS | 1261.8 | 15 | No | No | No | -0.16% | 2.4 | No |
| LT.NS | 3990.0 | 10 | No | No | No | -0.23% | 0.61 | No |
| RELIANCE.NS | 1290.9 | 0 | No | No | No | -1.49% | 1.66 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.