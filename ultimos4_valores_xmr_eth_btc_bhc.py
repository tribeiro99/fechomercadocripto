import vectorbt as vbt
import pandas as pd


cript_price = vbt.YFData.download(
        ["BTC-EUR", "XMR-EUR", "ETH-EUR","BCH-EUR"],
        missing_index='drop').get("Close")

print(cript_price.tail(4))

