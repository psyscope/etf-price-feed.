# Stocks paper bot log

Simulation only: no real orders, no broker paper accounts, no sign-ins.
Prices: this repo's data/<TICKER>.csv (adj_close), refreshed weekdays 22:30 UTC by the Daily ETF closes job.
Run: weekdays, Fri Nov 20 to Fri Dec 18, 2026 (4 weeks). Start equity $10,000 per account.
Fills at that day's adjusted close, no fees, cash earns 0%. State: state.json (same folder).

Accounts:
1. SPY 10-month SMA filter: hold SPY when last month-end close is above the 10-month SMA of month-end closes, else cash. Checked at month-end only.
2. QQQ 50/200-day crossover: hold QQQ when 50-day SMA > 200-day SMA, else cash.
3. SPY buy and hold.
4. QQQ buy and hold.
5. ETF basket 12-month trend: SPY, EFA, TLT, IEF, GLD, DBC. Slices inverse to 60-day volatility, summing to 100%. Hold a slice only when its 12-month total return is positive, else that slice is cash. Rebalance at each month-end close.
6. SPY Nov-Apr seasonal: hold SPY from November through April, cash May through October.

## Daily log

### Fri Nov 20, 2026: opened all six at the close
Closes: SPY 689.81, QQQ 608.45, EFA 96.14, TLT 81.45, IEF 91.65, GLD 322.87, DBC 29.32.
1. SPY 10-month SMA: Oct month-end 755.72 above SMA 725.56, so 100% SPY (14.4967 sh). Equity $10,000.
2. QQQ 50/200: 50-day 710.88 above 200-day 682.07, so 100% QQQ (16.4352 sh). Equity $10,000.
3. SPY buy and hold: 100% SPY (14.4967 sh). Equity $10,000.
4. QQQ buy and hold: 100% QQQ (16.4352 sh). Equity $10,000.
5. ETF basket: 12-month returns SPY +6.9%, EFA +9.0%, DBC +33.6% (held); TLT -4.4%, IEF -1.6%, GLD -13.9% (cash). Slices SPY 12.5%, EFA 13.5%, DBC 11.5%; 62.5% cash. Equity $10,000.
6. SPY Nov-Apr seasonal: November, so 100% SPY (14.4967 sh). Equity $10,000.
Note: QQQ closed well below its 50-day average (608 vs 711) after a sharp week; the crossover rule still says hold.
