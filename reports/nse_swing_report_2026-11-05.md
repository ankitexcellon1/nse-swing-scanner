# NSE Swing Scanner Report

Report date: 2026-11-05
Run time: 2026-11-05 01:54 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 23810.85
- Nifty return: 1.58%
- Nifty EMA20: 22988.99
- Nifty EMA50: 23195.8
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 2
- Passed volume filter: 3
- Passed relative strength filter: 5
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 80/100
- Close: 1424.5
- Setup type: Breakout / momentum continuation
- RSI14: 64.61
- Volume vs AvgVol20: 17496620 vs 12574393
- Relative strength vs Nifty: 1.09%
- Nearest support: 1303.7
- Nearest resistance: 1411.8
- Stop-loss: 1382.06
- Target 1: 1509.38
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: No
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: Yes

Why not a final candidate:
- Volume failed: volume is not above 1.5x 20-day average volume.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Bharti Airtel (BHARTIARTL.NS)
- Score: 75/100
- Close: 2065.0
- Setup type: Breakout / momentum continuation
- RSI14: 81.59
- Volume vs AvgVol20: 18603124 vs 9596109
- Relative strength vs Nifty: 2.19%
- Nearest support: 1742.3
- Nearest resistance: 2000.9
- Stop-loss: 1987.94
- Target 1: 2219.11
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: No
- Risk-reward pass: Yes

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Overextension risk: price is too far from EMA20 or RSI is too high.

IQ200 Red-Team Review:
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Overextension concern: entry may be late; wait for pullback or fresh confirmation.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Infosys (INFY.NS)
- Score: 40/100
- Close: 1148.1
- Setup type: Trend watchlist / below resistance
- RSI14: 62.81
- Volume vs AvgVol20: 10495455 vs 16635546
- Relative strength vs Nifty: -2.69%
- Nearest support: 990.1
- Nearest resistance: 1197.8
- Stop-loss: 1074.55
- Target 1: 1197.8
- Risk-reward: 0.68

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
- Reliance Industries (RELIANCE.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.
- ITC (ITC.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Tata Consultancy Services (TCS.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- State Bank of India (SBIN.NS): Score 20/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1424.5 | 80 | Yes | Yes | No | 1.09% | 2.0 | No |
| BHARTIARTL.NS | 2065.0 | 75 | Yes | No | Yes | 2.19% | 2.0 | No |
| INFY.NS | 1148.1 | 40 | Yes | Yes | No | -2.69% | 0.68 | No |
| RELIANCE.NS | 1307.9 | 35 | No | No | Yes | -0.97% | 2.0 | No |
| ITC.NS | 273.9 | 30 | No | No | No | 1.24% | 2.0 | No |
| TCS.NS | 2499.1 | 25 | Yes | No | No | -1.68% | 1.15 | No |
| SBIN.NS | 970.25 | 20 | No | No | Yes | -3.28% | 0.57 | No |
| HDFCBANK.NS | 725.5 | 15 | No | No | No | 2.06% | 0.42 | No |
| AXISBANK.NS | 1232.7 | 15 | No | No | No | 0.38% | 1.71 | No |
| LT.NS | 3948.2 | 0 | No | No | No | -1.37% | 0.04 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.