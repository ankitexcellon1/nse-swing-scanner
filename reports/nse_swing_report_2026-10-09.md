# NSE Swing Scanner Report

Report date: 2026-10-09
Run time: 2026-10-09 00:43 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 22603.05
- Nifty return: -0.76%
- Nifty EMA20: 23072.31
- Nifty EMA50: 23518.75
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 0
- Passed momentum filter: 0
- Passed volume filter: 5
- Passed relative strength filter: 5
- Passed risk-reward filter: 6
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only
No watchlist candidates.

## Rejected Stocks
- State Bank of India (SBIN.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.
- ICICI Bank (ICICIBANK.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Bharti Airtel (BHARTIARTL.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Tata Consultancy Services (TCS.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| SBIN.NS | 954.0 | 50 | No | No | Yes | 0.26% | 7.1 | No |
| ICICIBANK.NS | 1357.5 | 35 | No | No | Yes | 1.85% | 1.46 | No |
| BHARTIARTL.NS | 1833.9 | 35 | No | No | Yes | 2.05% | 1.2 | No |
| ITC.NS | 265.7 | 35 | No | No | Yes | 0.39% | 0.7 | No |
| AXISBANK.NS | 1242.5 | 35 | No | No | Yes | 0.32% | 0.4 | No |
| RELIANCE.NS | 1207.7 | 15 | No | No | No | -0.09% | 2.91 | No |
| TCS.NS | 2080.3 | 15 | No | No | No | -0.18% | 5.07 | No |
| INFY.NS | 992.0 | 15 | No | No | No | -1.4% | 9.11 | No |
| HDFCBANK.NS | 702.75 | 15 | No | No | No | -0.46% | 2.23 | No |
| LT.NS | 3701.5 | 15 | No | No | No | -1.06% | 6.99 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.