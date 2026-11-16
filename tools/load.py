"""M1 tarixni yuklash va boshqa timeframe'ga o'girish.

Misol:
    from tools.load import load_m1, resample
    df = load_m1("XAUUSD", 2020, 2026)      # M1 barlar
    h1 = resample(df, "1h")                  # H1 barlar
"""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data" / "M1"


def load_m1(symbol: str, year_from: int = 2020, year_to: int = 2100) -> pd.DataFrame:
    files = sorted(
        f for f in (DATA / symbol).glob(f"{symbol}_M1_*.csv.gz")
        if year_from <= int(f.stem.split("_")[-1].split(".")[0]) <= year_to
    )
    if not files:
        raise FileNotFoundError(f"{symbol}: {DATA / symbol} ichida fayl yo'q")
    df = pd.concat((pd.read_csv(f, parse_dates=["time"]) for f in files), ignore_index=True)
    return df.set_index("time").sort_index()


def resample(df: pd.DataFrame, rule: str) -> pd.DataFrame:
    """rule: '5min', '15min', '30min', '1h', '4h', '1D'"""
    out = df.resample(rule, label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "tick_volume": "sum"}
    )
    return out.dropna(subset=["open"])


if __name__ == "__main__":
    import sys
    sym = sys.argv[1] if len(sys.argv) > 1 else "XAUUSD"
    d = load_m1(sym)
    print(sym, len(d), "bar", d.index[0], "->", d.index[-1])
    print(d.tail(3))
