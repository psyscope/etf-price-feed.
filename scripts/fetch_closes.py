"""Download daily closes for the paper bot's ETFs and save one CSV per ticker.

Columns: date, close (raw close), adj_close (split and dividend adjusted).
Keeps full history from 2015 so 200-day and 12-month signals have room.
"""
import pathlib
import sys

import yfinance as yf

TICKERS = ["SPY", "QQQ", "EFA", "TLT", "IEF", "GLD", "DBC"]
START = "2015-01-01"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    failed = []
    for t in TICKERS:
        df = yf.download(t, start=START, auto_adjust=False, progress=False, threads=False)
        if df is None or df.empty:
            failed.append(t)
            continue
        if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
            df.columns = df.columns.get_level_values(0)
        out = df[["Close", "Adj Close"]].rename(columns={"Close": "close", "Adj Close": "adj_close"})
        out.index.name = "date"
        out = out.dropna().round(4)
        out.to_csv(OUT / f"{t}.csv")
        print(f"{t}: {len(out)} rows, last {out.index[-1].date()} adj_close {out['adj_close'].iloc[-1]}")
    if failed:
        print("FAILED:", ", ".join(failed), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
