import vectorbt as vbt
import pandas as pd 

 
cripto_price =vbt.YFData.download(
        ["BTC-EUR","ETH-EUR","XMR.EUR"],
        missing_index='drop').get("Close")

print(cripto_price.tail())
 


