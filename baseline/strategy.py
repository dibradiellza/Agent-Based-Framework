import pandas as pd
import numpy as np

FEE_RATE = 0.001


def run_strategy(df):
    df = df.copy()

    df["ma20"] = df["close"].rolling(20).mean()
    df["ma50"] = df["close"].rolling(50).mean()

    df["signal"] = 0
    df.loc[df["ma20"] > df["ma50"], "signal"] = 1
    df.loc[df["ma20"] <= df["ma50"], "signal"] = -1

    df["returns"] = df["close"].pct_change()
    trades = df["signal"].diff().abs() > 0

    df["strategy_returns"] = (
        df["signal"].shift(1) * df["returns"]
        - trades.shift(1).fillna(False).astype(float) * FEE_RATE
    )

    df = df.dropna()

    return df
