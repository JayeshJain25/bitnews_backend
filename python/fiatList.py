import pandas as pd
import ccy
from forex_python.converter import CurrencyRates
import flag
import csv

c = CurrencyRates()
data = c.get_rates('USD')
df = pd.DataFrame(data, index=[False])

df.rename(index={0: 'Currency'}, inplace=True)
df = df.transpose()

df.reset_index(inplace=True)

df.columns = ['symbol', 'price']

df = df.drop(df.index[11])

countryName = []
default_country = []
flagList = []

for symi in df['symbol']:
    c = ccy.currency(symi)
    countryName.append(c.name)

for symbol in df['symbol']:
    c = ccy.currency(symbol)
    default_country.append(c.default_country)

for countryName1 in default_country:
    flagList.append(flag.flag(countryName1))

df['name'] = countryName
df['id'] = countryName
df['image'] = flagList
df['type'] = "Fiat"

df.loc[len(df.index)] = ['USD', 1, "US Dollar", "US Dollar", "🇺🇸","Fiat"]

df.to_csv('fiatPrices.csv', index=False)

