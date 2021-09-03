import pandas as pd
from pycoingecko import CoinGeckoAPI

# initialising coingeckoAPI
cg = CoinGeckoAPI()

# getting coins data
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=1)

df = pd.DataFrame(coin_list)
list = []
list1 = []

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

    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)

# making a dataframe of fetched data
df1 = pd.DataFrame(list)
dfCoin1 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=2)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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

    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)

df2 = pd.DataFrame(list)
dfCoin2 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=3)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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

    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)

df3 = pd.DataFrame(list)
dfCoin3 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=4)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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

    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)

df4 = pd.DataFrame(list)
dfCoin4 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=5)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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

    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df5 = pd.DataFrame(list)
dfCoin5 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=6)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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

    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)

df6 = pd.DataFrame(list)
dfCoin6 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=7)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df7 = pd.DataFrame(list)
dfCoin7 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=8)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df8 = pd.DataFrame(list)
dfCoin8 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=9)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df9 = pd.DataFrame(list)
dfCoin9 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=10)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df10 = pd.DataFrame(list)
dfCoin10 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=11)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df11 = pd.DataFrame(list)
dfCoin11 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=12)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df12 = pd.DataFrame(list)
dfCoin12 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=13)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df13 = pd.DataFrame(list)
dfCoin13 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=14)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df14 = pd.DataFrame(list)
dfCoin14 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=15)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df15 = pd.DataFrame(list)
dfCoin15 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=16)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df16 = pd.DataFrame(list)
dfCoin16 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=17)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df17 = pd.DataFrame(list)
dfCoin17 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=18)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df18 = pd.DataFrame(list)
dfCoin18 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=19)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df19 = pd.DataFrame(list)
dfCoin19 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=20)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df20 = pd.DataFrame(list)
dfCoin20 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=21)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df21 = pd.DataFrame(list)
dfCoin21 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=22)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df22 = pd.DataFrame(list)
dfCoin22 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=23)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df23 = pd.DataFrame(list)
dfCoin23 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=24)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df24 = pd.DataFrame(list)
dfCoin24 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=25)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df25 = pd.DataFrame(list)
dfCoin25 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=26)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df26 = pd.DataFrame(list)
dfCoin26 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=27)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df27 = pd.DataFrame(list)
dfCoin27 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=28)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df28 = pd.DataFrame(list)
dfCoin28 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=29)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df29 = pd.DataFrame(list)
dfCoin29 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=30)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df30 = pd.DataFrame(list)
dfCoin30 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=31)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df31 = pd.DataFrame(list)
dfCoin31 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=32)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df32 = pd.DataFrame(list)
dfCoin32 = pd.DataFrame(list1)

coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=33)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df33 = pd.DataFrame(list)
dfCoin33 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=30)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df34 = pd.DataFrame(list)
dfCoin34 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=35)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df35 = pd.DataFrame(list)
dfCoin35 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=36)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df36 = pd.DataFrame(list)
dfCoin36 = pd.DataFrame(list1)
coin_list = cg.get_coins_markets(vs_currency='inr', per_page=250, page=37)
df = pd.DataFrame(coin_list)
list = []
list1 = []
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
    dict1 = {'id': df['id'][ind], 'symbol': df['symbol'][ind], 'name': df['name'][ind],
             'price': df['current_price'][ind],
             'market_cap': df['market_cap'][ind], 'total_volume': df['total_volume'][ind],
             'rank': df['market_cap_rank'][ind], 'image': df['image'][ind]}

    list1.append(dict1)
df37 = pd.DataFrame(list)
dfCoin37 = pd.DataFrame(list1)
# making a list of all dataframes
df = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20,
      df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31, df32, df33, df34, df35, df36, df37]

dfCoin = [dfCoin1, dfCoin2, dfCoin3, dfCoin4, dfCoin5, dfCoin6, dfCoin7, dfCoin8, dfCoin9, dfCoin10, dfCoin11, dfCoin12,
          dfCoin13,
          dfCoin14, dfCoin15, dfCoin16, dfCoin17, dfCoin18, dfCoin19, dfCoin20,
          dfCoin21, dfCoin22, dfCoin23, dfCoin24, dfCoin25, dfCoin26, dfCoin27, dfCoin28, dfCoin29, dfCoin30, dfCoin31,
          dfCoin32, dfCoin33, dfCoin34, dfCoin35, dfCoin36, dfCoin37]

# concatenating the list of dataframes
result = pd.concat(df)
result1 = pd.concat(dfCoin)

# saving to .csv file
result.to_csv("cryptoCoinsMarketData.csv", index=False)
result1.to_csv("cryptoCurrencyPrices.csv", index=False)
