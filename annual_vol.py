#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:43:29 2024

@author: louisfavreau
"""

import pandas as pd
import numpy as np
import yfinance as yf

sp500= yf.download("ES=F")

prices = sp500["Adj Close"]
sp500["Log Returns"] = np.log(prices).diff()
annual_vol = sp500["Log Returns"].std() * np.sqrt(252)

print(f"annualized volatility: {annual_vol}")