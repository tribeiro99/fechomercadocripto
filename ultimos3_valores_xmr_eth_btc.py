import vectorbt as vbt
import pandas as pd 

eth_price =vbt.YFData.download(
        "ETH-EUR",
        missing_index='drop').get("Close")

print(eth_price.tail())
 
btc_price =vbt.YFData.download(
        "BTC-EUR",
        missing_index='drop').get("Close")

print(btc_price.tail())
 



xmr_price =vbt.YFData.download(
        "XMR-EUR",
        missing_index='drop').get("Close")

print(xmr_price.tail())
 

