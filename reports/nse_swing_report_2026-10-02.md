# NSE Swing Scanner Report

Report date: 2026-10-02
Run time: 2026-10-02 23:47 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Risky environment; avoid aggressive fresh longs
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 22421.95
- Nifty return: -0.88%
- Nifty EMA20: 23221.49
- Nifty EMA50: 23630.09
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 0
- Passed momentum filter: 1
- Passed volume filter: 2
- Passed relative strength filter: 6
- Passed risk-reward filter: 4
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only
No watchlist candidates.

## Rejected Stocks
- Infosys (INFY.NS): Score 50/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- HDFC Bank (HDFCBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ICICI Bank (ICICIBANK.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- State Bank of India (SBIN.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- ITC (ITC.NS): Score 20/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Reliance Industries (RELIANCE.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Bharti Airtel (BHARTIARTL.NS): Score 0/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| INFY.NS | 1035.0 | 50 | No | No | Yes | 4.99% | 2.91 | No |
| TCS.NS | 2075.0 | 30 | No | No | No | 2.07% | 6.78 | No |
| HDFCBANK.NS | 721.2 | 30 | No | Yes | No | 2.64% | 1.36 | No |
| ICICIBANK.NS | 1310.6 | 30 | No | No | No | 0.04% | 7.21 | No |
| SBIN.NS | 954.1 | 30 | No | No | No | 0.32% | 74.46 | No |
| ITC.NS | 255.9 | 20 | No | No | Yes | -1.73% | 0 | No |
| AXISBANK.NS | 1217.1 | 15 | No | No | No | 0.15% | 1.66 | No |
| RELIANCE.NS | 1167.7 | 0 | No | No | No | -0.75% | 0 | No |
| LT.NS | 3693.4 | 0 | No | No | No | -0.89% | 0 | No |
| BHARTIARTL.NS | 1741.1 | 0 | No | No | No | -0.02% | 0 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.