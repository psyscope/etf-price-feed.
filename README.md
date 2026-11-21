# ETF price feed

Daily closes for SPY, QQQ, EFA, TLT, IEF, GLD and DBC, saved by a GitHub Actions job every weekday after the US close. Used by the stocks paper bot (simulation only).

Files: data/<TICKER>.csv with columns date, close, adj_close. History from 2015.
Run it by hand from the Actions tab ("Daily ETF closes", Run workflow).
