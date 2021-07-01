import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
coin_list = cg.get_coins_markets(vs_currency = 'inr')
df = pd.DataFrame(coin_list)
var = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'market_cap_rank', 'image']]
list=[]
for ind in df.index:
    dict= {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind], 'price': df['current_price'][ind],
           'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
           'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}
    list.append(dict)
news_df=pd.DataFrame(list)
news_df.to_csv("cryptoCurrencyPrices.csv", index=False)
