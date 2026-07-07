# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:57:43 2026

@author: diell
"""

import numpy as np

def evaluate(df):
    r = df["strategy_returns"]
    total_return = (1 + r).prod() - 1
    sharpe = (r.mean() / r.std()) * np.sqrt(24 * 365) if r.std() > 0 else 0
    max_drawdown = ((1 + r).cumprod() / (1 + r).cumprod().cummax() - 1).min()
    calmar = (total_return / abs(max_drawdown)) if max_drawdown != 0 else 0

    return {
        "sharpe":        round(sharpe, 4),
        "calmar":        round(calmar, 4),
        "total_return":  round(total_return * 100, 2),
        "max_drawdown":  round(max_drawdown * 100, 2)
    }