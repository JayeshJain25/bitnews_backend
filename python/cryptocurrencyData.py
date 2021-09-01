import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250)
df = pd.DataFrame(coin_list)
var = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'market_cap_rank', 'image', 'high_24h',
          'low_24h', 'price_change_24h', 'price_change_percentage_24h', 'market_cap_change_24h',
          'market_cap_change_percentage_24h', 'circulating_supply',
          'total_supply', 'max_supply', 'atl', 'atl_change_percentage', 'atl_date', 'last_updated']]
list = []
for ind in df.index:
    dict = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
            'price': df['current_price'][ind],
            'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
            'rank': df['market_cap_rank'][ind], 'image': df['image'][ind], 'high_24h': df['high_24h'][ind],
            'low_24h': df['low_24h'][ind], 'price_change_24h': df['price_change_24h'][ind],
            'price_change_percentage_24h': df['price_change_percentage_24h'][ind],
            'market_cap_change_24h': df['market_cap_change_24h'][ind],
            'market_cap_change_percentage_24h': df['market_cap_change_percentage_24h'][ind],
            'circulating_supply': df['circulating_supply'][ind],
            'total_supply': df['total_supply'][ind],
            'max_supply': df['max_supply'][ind],
            'atl': df['atl'][ind],
            'atl_change_percentage': df['atl_change_percentage'][ind],
            'atl_date': df['atl_date'][ind],
            'last_updated': df['last_updated'][ind],
            }
    list.append(dict)
news_df = pd.DataFrame(list)
news_df.to_csv("cryptoCoinsMarketData.csv", index=False)
