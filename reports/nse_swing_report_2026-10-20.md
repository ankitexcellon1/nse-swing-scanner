# NSE Swing Scanner Report

Report date: 2026-10-20
Run time: 2026-10-20 23:22 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 22888.95
- Nifty return: -1.11%
- Nifty EMA20: 22891.8
- Nifty EMA50: 23297.35
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 1
- Passed momentum filter: 5
- Passed volume filter: 4
- Passed relative strength filter: 5
- Passed risk-reward filter: 1
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### Tata Consultancy Services (TCS.NS)
- Score: 60/100
- Close: 2460.9
- Setup type: Trend watchlist / below resistance
- RSI14: 81.79
- Volume vs AvgVol20: 8676373 vs 5449742
- Relative strength vs Nifty: 0.94%
- Nearest support: 2032.4
- Nearest resistance: 2484.7
- Stop-loss: 2344.3
- Target 1: 2484.7
- Risk-reward: 0.2

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: No
- Risk-reward pass: No

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Overextension risk: price is too far from EMA20 or RSI is too high.
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Overextension concern: entry may be late; wait for pullback or fresh confirmation.
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Rejected Stocks
- State Bank of India (SBIN.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ICICI Bank (ICICIBANK.NS): Score 45/100. Technical trend failed: price/EMA structure is not clean.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Bharti Airtel (BHARTIARTL.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| TCS.NS | 2460.9 | 60 | Yes | No | Yes | 0.94% | 0.2 | No |
| SBIN.NS | 973.7 | 50 | No | Yes | Yes | 2.26% | 1.02 | No |
| ICICIBANK.NS | 1381.0 | 45 | No | Yes | Yes | -0.04% | 0.44 | No |
| AXISBANK.NS | 1236.0 | 35 | No | Yes | Yes | -3.08% | 1.32 | No |
| LT.NS | 3661.9 | 30 | No | No | No | 2.07% | 4.1 | No |
| RELIANCE.NS | 1202.0 | 15 | No | No | No | 0.35% | 1.34 | No |
| INFY.NS | 1130.7 | 15 | No | Yes | No | -1.52% | 0.72 | No |
| BHARTIARTL.NS | 1875.2 | 15 | No | Yes | No | -0.45% | 0.52 | No |
| ITC.NS | 260.8 | 15 | No | No | No | 0.09% | 1.34 | No |
| HDFCBANK.NS | 712.0 | 0 | No | No | No | -1.2% | 1.73 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.