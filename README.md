# historyfx

M1 OHLC history (Exness-MT5Real32, server time, 2020 -> 2026-10) for backtesting.
Copied from L1rikfx/back-test `data/`.

- `data/M1/<SYMBOL>/<SYMBOL>_M1_<YEAR>.csv.gz` — columns: time,open,high,low,close,tick_volume
- `data/TICK/XAUUSD_exness/` — XAUUSD ticks
- No spread in data; pass it as a backtest parameter.
- Loader: `tools/load.py` (`load_m1`, `resample`).
