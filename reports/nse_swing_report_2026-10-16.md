# NSE Swing Scanner Report

Report date: 2026-10-16
Run time: 2026-10-16 22:45 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Neutral / data-limited environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 23146.15
- Nifty return: 0.65%
- Nifty EMA20: 22892.1
- Nifty EMA50: 23314.01
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 0
- Passed momentum filter: 2
- Passed volume filter: 3
- Passed relative strength filter: 3
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
- Bharti Airtel (BHARTIARTL.NS): Score 75/100. Technical trend failed: price/EMA structure is not clean.
- Tata Consultancy Services (TCS.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Overextension risk: price is too far from EMA20 or RSI is too high.
- Infosys (INFY.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Overextension risk: price is too far from EMA20 or RSI is too high.
- ICICI Bank (ICICIBANK.NS): Score 40/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Larsen & Toubro (LT.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.
- Axis Bank (AXISBANK.NS): Score 10/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- State Bank of India (SBIN.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| BHARTIARTL.NS | 1905.0 | 75 | No | Yes | Yes | 2.1% | 2.0 | No |
| TCS.NS | 2465.0 | 50 | No | No | Yes | 4.24% | 2.0 | No |
| INFY.NS | 1161.2 | 50 | No | No | Yes | 3.96% | 2.0 | No |
| ICICIBANK.NS | 1397.0 | 40 | No | Yes | No | -0.1% | 2.0 | No |
| LT.NS | 3627.1 | 15 | No | No | No | -0.78% | 9.3 | No |
| AXISBANK.NS | 1290.0 | 10 | No | No | No | -0.49% | 0.1 | No |
| RELIANCE.NS | 1211.2 | 0 | No | No | No | -0.96% | 1.11 | No |
| HDFCBANK.NS | 728.85 | 0 | No | No | No | -0.37% | 0.89 | No |
| SBIN.NS | 962.6 | 0 | No | No | No | -0.38% | 1.53 | No |
| ITC.NS | 263.5 | 0 | No | No | No | -0.8% | 0.73 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.