# NSE Swing Scanner Report

Report date: 2026-07-15
Run time: 2026-07-15 20:24 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 24078.5
- Nifty return: -0.55%
- Nifty EMA20: 24033.97
- Nifty EMA50: 23951.11
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 4
- Passed momentum filter: 5
- Passed volume filter: 2
- Passed relative strength filter: 7
- Passed risk-reward filter: 3
- Final qualified candidates: 0

## Executive Summary
No clean qualified swing-trading candidate found today under the defined MVP rules.
The system did not force recommendations. Watchlist names are not buy calls.

## Final Qualified Candidates

No clean qualified swing-trading candidate found today under the defined rules.

## Watchlist / Manual Review Only

### ICICI Bank (ICICIBANK.NS)
- Score: 65/100
- Close: 1416.2
- Setup type: Trend watchlist / below resistance
- RSI14: 59.59
- Volume vs AvgVol20: 12960233 vs 12060154
- Relative strength vs Nifty: 1.15%
- Nearest support: 1331.4
- Nearest resistance: 1433.0
- Stop-loss: 1381.22
- Target 1: 1433.0
- Risk-reward: 0.48

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

### HDFC Bank (HDFCBANK.NS)
- Score: 55/100
- Close: 815.45
- Setup type: Trend watchlist / below resistance
- RSI14: 60.04
- Volume vs AvgVol20: 21487188 vs 34032999
- Relative strength vs Nifty: 1.3%
- Nearest support: 772.55
- Nearest resistance: 843.0
- Stop-loss: 795.06
- Target 1: 843.0
- Risk-reward: 1.35

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
- Close: 1030.1
- Setup type: Trend watchlist / below resistance
- RSI14: 44.34
- Volume vs AvgVol20: 14274423 vs 10426132
- Relative strength vs Nifty: 2.0%
- Nearest support: 1011.4
- Nearest resistance: 1059.8
- Stop-loss: 1011.4
- Target 1: 1059.8
- Risk-reward: 1.59

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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 50/100
- Close: 1918.3
- Setup type: Trend watchlist / below resistance
- RSI14: 63.14
- Volume vs AvgVol20: 5762680 vs 6615824
- Relative strength vs Nifty: -0.39%
- Nearest support: 1833.1
- Nearest resistance: 1966.0
- Stop-loss: 1864.89
- Target 1: 1966.0
- Risk-reward: 0.89

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
- Axis Bank (AXISBANK.NS): Score 60/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.
- Reliance Industries (RELIANCE.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Tata Consultancy Services (TCS.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 30/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.
- Larsen & Toubro (LT.NS): Score 20/100. Technical trend failed: price/EMA structure is not clean.; Momentum failed: RSI is outside preferred 55-70 range.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Infosys (INFY.NS): Score 15/100. Technical trend failed: price/EMA structure is not clean.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| ICICIBANK.NS | 1416.2 | 65 | Yes | Yes | No | 1.15% | 0.48 | No |
| AXISBANK.NS | 1312.3 | 60 | No | No | Yes | 0.15% | 4.37 | No |
| HDFCBANK.NS | 815.45 | 55 | Yes | Yes | No | 1.3% | 1.35 | No |
| SBIN.NS | 1030.1 | 50 | Yes | No | No | 2.0% | 1.59 | No |
| BHARTIARTL.NS | 1918.3 | 50 | Yes | Yes | No | -0.39% | 0.89 | No |
| RELIANCE.NS | 1295.5 | 30 | No | No | No | 0.74% | 2.07 | No |
| TCS.NS | 2189.2 | 30 | No | Yes | No | 0.03% | 0.44 | No |
| ITC.NS | 276.65 | 30 | No | No | No | 0.95% | 10.85 | No |
| LT.NS | 3783.9 | 20 | No | No | Yes | -1.13% | 0 | No |
| INFY.NS | 1076.3 | 15 | No | Yes | No | -0.97% | 1.87 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.