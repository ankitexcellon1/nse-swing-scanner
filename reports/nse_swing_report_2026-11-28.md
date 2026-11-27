# NSE Swing Scanner Report

Report date: 2026-11-28
Run time: 2026-11-28 03:35 IST
Universe intended: Nifty 50
Universe source: Fallback test universe; official Nifty 50 CSV fetch failed: Remote end closed connection without response
Stocks verified: 10
Market condition: Bullish to selective swing environment
Data confidence: Medium
Report status: Technical MVP / Data-limited

## Benchmark Context
- Nifty close: 25884.5
- Nifty return: 0.25%
- Nifty EMA20: 24862.96
- Nifty EMA50: 24147.86
- Note: Market condition is based only on Nifty price/EMA context. Breadth and sector data are not included in this MVP.

## Scan Funnel
- Stocks with verified OHLC: 10
- Stocks with computed EMA/RSI/ATR: 10
- Passed technical filter: 10
- Passed momentum filter: 4
- Passed volume filter: 3
- Passed relative strength filter: 4
- Passed risk-reward filter: 3
- Final qualified candidates: 1

## Executive Summary
1 stock(s) passed all MVP technical filters. These are research candidates only and still require manual chart, delivery, news, and event-risk confirmation.

## Final Qualified Candidates

### Tata Consultancy Services (TCS.NS)
- Setup type: Breakout / momentum continuation
- Close: 2640.3
- Buy zone: Near 2640.3 only after price confirmation
- Stop-loss: 2532.29
- Target 1: 2856.32
- Risk-reward: 2.0
- Score: 100/100

Evidence:
- EMA20: 2444.97, EMA50: 2378.35, EMA200: 2448.84
- RSI14: 69.68
- Volume: 5534593, AvgVol20: 3603770
- Relative strength vs Nifty: 4.64%

IQ200 Red-Team Review:
- No major technical objection found in MVP filters, but manual chart/news confirmation is still required.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

## Watchlist / Manual Review Only

### Infosys (INFY.NS)
- Score: 75/100
- Close: 1183.0
- Setup type: Trend watchlist / below resistance
- RSI14: 61.29
- Volume vs AvgVol20: 16676971 vs 11009910
- Relative strength vs Nifty: 4.44%
- Nearest support: 1072.6
- Nearest resistance: 1198.8
- Stop-loss: 1133.18
- Target 1: 1198.8
- Risk-reward: 0.32

Pass/Fail:
- Technical pass: Yes
- Momentum pass: Yes
- Volume pass: Yes
- Relative strength pass: Yes
- Not overextended: Yes
- Risk-reward pass: No

Why not a final candidate:
- Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

IQ200 Red-Team Review:
- Trade-plan concern: target versus stop-loss does not justify the risk.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### HDFC Bank (HDFCBANK.NS)
- Score: 75/100
- Close: 862.0
- Setup type: Breakout / momentum continuation
- RSI14: 79.14
- Volume vs AvgVol20: 70517167 vs 43509005
- Relative strength vs Nifty: 1.62%
- Nearest support: 669.2
- Nearest resistance: 859.7
- Stop-loss: 827.43
- Target 1: 931.14
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

### Reliance Industries (RELIANCE.NS)
- Score: 55/100
- Close: 1396.2
- Setup type: Breakout / momentum continuation
- RSI14: 79.14
- Volume vs AvgVol20: 20028816 vs 21909914
- Relative strength vs Nifty: 1.37%
- Nearest support: 1152.5
- Nearest resistance: 1394.2
- Stop-loss: 1353.86
- Target 1: 1480.89
- Risk-reward: 2.0

Pass/Fail:
- Technical pass: Yes
- Momentum pass: No
- Volume pass: No
- Relative strength pass: Yes
- Not overextended: No
- Risk-reward pass: Yes

Why not a final candidate:
- Momentum failed: RSI is outside preferred 55-70 range.
- Volume failed: volume is not above 1.5x 20-day average volume.
- Overextension risk: price is too far from EMA20 or RSI is too high.

IQ200 Red-Team Review:
- Main objection: volume confirmation is weak, so breakout/follow-through may fail.
- Momentum caution: RSI is above the preferred range, so chasing may be risky.
- Overextension concern: entry may be late; wait for pullback or fresh confirmation.
- Avoid entry if the stock opens with a large gap-up, fails near resistance, or market direction turns weak.

### Larsen & Toubro (LT.NS)
- Score: 50/100
- Close: 4132.1
- Setup type: Trend watchlist / below resistance
- RSI14: 65.6
- Volume vs AvgVol20: 1202942 vs 2298981
- Relative strength vs Nifty: -0.83%
- Nearest support: 3648.3
- Nearest resistance: 4259.0
- Stop-loss: 4004.56
- Target 1: 4259.0
- Risk-reward: 0.99

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

### Bharti Airtel (BHARTIARTL.NS)
- Score: 50/100
- Close: 2102.5
- Setup type: Trend watchlist / below resistance
- RSI14: 55.56
- Volume vs AvgVol20: 3946729 vs 8470457
- Relative strength vs Nifty: -0.96%
- Nearest support: 1910.6
- Nearest resistance: 2172.9
- Stop-loss: 2035.4
- Target 1: 2172.9
- Risk-reward: 1.05

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
- ICICI Bank (ICICIBANK.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- Axis Bank (AXISBANK.NS): Score 35/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- State Bank of India (SBIN.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.
- ITC (ITC.NS): Score 25/100. Momentum failed: RSI is outside preferred 55-70 range.; Volume failed: volume is not above 1.5x 20-day average volume.; Relative strength failed: stock did not outperform Nifty.; Overextension risk: price is too far from EMA20 or RSI is too high.; Risk-reward failed: setup does not offer minimum 1:2 risk-reward.

## Full Scan Table

| Symbol | Close | Score | Tech | RSI | Vol | RS vs Nifty | RR | Qualified |
|---|---:|---:|---|---|---|---:|---:|---|
| TCS.NS | 2640.3 | 100 | Yes | Yes | Yes | 4.64% | 2.0 | Yes |
| INFY.NS | 1183.0 | 75 | Yes | Yes | Yes | 4.44% | 0.32 | No |
| HDFCBANK.NS | 862.0 | 75 | Yes | No | Yes | 1.62% | 2.0 | No |
| RELIANCE.NS | 1396.2 | 55 | Yes | No | No | 1.37% | 2.0 | No |
| LT.NS | 4132.1 | 50 | Yes | Yes | No | -0.83% | 0.99 | No |
| BHARTIARTL.NS | 2102.5 | 50 | Yes | Yes | No | -0.96% | 1.05 | No |
| ICICIBANK.NS | 1611.0 | 35 | Yes | No | No | -2.02% | 0.63 | No |
| AXISBANK.NS | 1408.0 | 35 | Yes | No | No | -0.96% | 0.83 | No |
| SBIN.NS | 1136.65 | 25 | Yes | No | No | -0.38% | 1.04 | No |
| ITC.NS | 307.0 | 25 | Yes | No | No | -0.98% | 0.58 | No |

## Data Limitations
- This MVP uses free public data through yfinance.
- Delivery percentage, official NSE bhavcopy, fundamentals, sector trend, market breadth, and news checks are not included yet.
- Relative strength is based only on one-day stock return versus one-day Nifty return.
- Support/resistance is approximated using the previous 20 trading days.
- Use this report for research only.

This is a swing-trading research shortlist, not a guaranteed buy/sell recommendation. Use manual confirmation, position sizing, and stop-loss discipline before taking any trade.