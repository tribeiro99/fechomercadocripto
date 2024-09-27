import vectorbt as vbt
import numpy as np
import pandas as pd

cript_price = vbt.YFData.download(
        ["BTC-EUR","XMR-EUR","ETH-EUR"],
        missing_index='drop').get("Close")

print(cript_price.tail())
 
