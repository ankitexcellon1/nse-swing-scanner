# NSE Swing Scanner Report

Report date: 2026-10-15
Run time: 2026-10-15 23:11 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Neutral / data-limited environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 22997.35
- Nifty return: 1.66%
- Nifty EMA20: 22865.36
- Nifty EMA50: 23320.85
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 0
- Passed momentum filter: 3
- Passed volume filter: 4
- Passed relative strength filter: 7
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
- ICICI Bank (ICICIBANK.NS): Score 75/100. Technical trend failed: price/EMA structure is not clean.
- Tata Consultancy Services (TCS.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Overextension risk: price is too far from EMA20 or RSI is too high.
- Bharti Airtel (BHARTIARTL.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 45/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.
- Reliance Industries (RELIANCE.NS): Score 35/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.
- HDFC Bank (HDFCBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- State Bank of India (SBIN.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1389.4 | 75 | No | Yes | Yes | 2.14% | 2.0 | No |
| TCS.NS | 2350.0 | 50 | No | No | Yes | 0.3% | 2.0 | No |
| BHARTIARTL.NS | 1854.0 | 50 | No | Yes | Yes | 1.65% | 0.69 | No |
| INFY.NS | 1110.0 | 45 | No | Yes | No | 0.36% | 2.0 | No |
| RELIANCE.NS | 1215.0 | 35 | No | No | Yes | 1.78% | 1.07 | No |
| AXISBANK.NS | 1288.0 | 30 | No | No | No | 0.19% | 2.0 | No |
| HDFCBANK.NS | 726.85 | 15 | No | No | No | 0.61% | 0.96 | No |
| LT.NS | 3632.0 | 15 | No | No | No | -1.93% | 8.01 | No |
| SBIN.NS | 960.0 | 0 | No | No | No | -1.13% | 1.82 | No |
| ITC.NS | 263.9 | 0 | No | No | No | -0.74% | 0.7 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.