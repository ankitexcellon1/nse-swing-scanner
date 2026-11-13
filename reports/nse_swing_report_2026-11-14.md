# NSE Swing Scanner Report

Report date: 2026-11-14
Run time: 2026-11-14 02:05 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 25299.35
- Nifty return: 0.18%
- Nifty EMA20: 23863.4
- Nifty EMA50: 23555.99
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 10
- Passed momentum filter: 0
- Passed volume filter: 1
- Passed relative strength filter: 5
- Passed risk-reward filter: 1
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### State Bank of India (SBIN.NS)
- Score: 75/100
- Close: 1086.5
- Setup type: Breakout / momentum continuation
- RSI14: 75.97
- Volume vs AvgVol20: 26973410 vs 14119693
- Relative strength vs Nifty: 2.2%
- Nearest support: 938.6
- Nearest resistance: 1077.95
- Stop-loss: 1048.69
- Target 1: 1162.11
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

## Rejected Stocks
- Reliance Industries (RELIANCE.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- HDFC Bank (HDFCBANK.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ICICI Bank (ICICIBANK.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 40/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Tata Consultancy Services (TCS.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Larsen & Toubro (LT.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Bharti Airtel (BHARTIARTL.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| SBIN.NS | 1086.5 | 75 | Yes | No | Yes | 2.2% | 2.0 | No |
| RELIANCE.NS | 1339.7 | 40 | Yes | No | No | 0.14% | 0.19 | No |
| HDFCBANK.NS | 812.3 | 40 | Yes | No | No | 0.53% | 0.21 | No |
| ICICIBANK.NS | 1590.0 | 40 | Yes | No | No | 0.99% | 0.5 | No |
| AXISBANK.NS | 1342.9 | 40 | Yes | No | No | 0.31% | 0.41 | No |
| TCS.NS | 2442.4 | 25 | Yes | No | No | -1.38% | 1.8 | No |
| INFY.NS | 1151.2 | 25 | Yes | No | No | -0.51% | 0.68 | No |
| LT.NS | 4159.2 | 25 | Yes | No | No | -1.43% | 0.75 | No |
| BHARTIARTL.NS | 2096.0 | 25 | Yes | No | No | -0.8% | 0.33 | No |
| ITC.NS | 284.05 | 25 | Yes | No | No | -0.51% | 0.2 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.