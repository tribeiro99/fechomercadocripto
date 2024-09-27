import vectorbt as vbt
import numpy as np
import pandas as pd


btc_price = vbt.YFData.download(
        ["BTC-EUR","XMR-EUR","ETH-EUR"],
        missing_index='drop').get("Close")

print(btc_price.tail())
 
