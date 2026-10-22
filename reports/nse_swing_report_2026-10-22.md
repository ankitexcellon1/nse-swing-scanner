# NSE Swing Scanner Report

Report date: 2026-10-22
Run time: 2026-10-22 23:26 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 22687.65
- Nifty return: -0.54%
- Nifty EMA20: 22865.42
- Nifty EMA50: 23255.13
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 1
- Passed momentum filter: 2
- Passed volume filter: 2
- Passed relative strength filter: 5
- Passed risk-reward filter: 5
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only
No watchlist candidates.

## Rejected Stocks
- Bharti Airtel (BHARTIARTL.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ICICI Bank (ICICIBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Axis Bank (AXISBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Tata Consultancy Services (TCS.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- State Bank of India (SBIN.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Infosys (INFY.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| BHARTIARTL.NS | 1895.0 | 50 | No | Yes | Yes | 0.71% | 0.49 | No |
| ICICIBANK.NS | 1398.5 | 40 | No | Yes | No | 1.51% | 0.33 | No |
| HDFCBANK.NS | 694.05 | 35 | No | No | Yes | -1.28% | 15.56 | No |
| LT.NS | 3638.3 | 30 | No | No | No | 0.6% | 6.76 | No |
| AXISBANK.NS | 1212.0 | 30 | No | No | No | 0.71% | 2.21 | No |
| TCS.NS | 2506.9 | 25 | Yes | No | No | -0.33% | 0.23 | No |
| RELIANCE.NS | 1184.5 | 15 | No | No | No | -1.49% | 2.11 | No |
| SBIN.NS | 970.0 | 15 | No | No | No | 1.27% | 1.09 | No |
| ITC.NS | 258.9 | 15 | No | No | No | -0.64% | 2.11 | No |
| INFY.NS | 1153.35 | 0 | No | No | No | -0.71% | 0.34 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.