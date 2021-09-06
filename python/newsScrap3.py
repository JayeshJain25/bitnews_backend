import time
import datetime
from dateutil.relativedelta import relativedelta
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk


def get_past_date(str_days_ago):
    TODAY = datetime.date.today()
    splitted = str_days_ago.split()
    if len(splitted) == 1 and splitted[0].lower() == 'today':
        return str(TODAY.isoformat())
    elif len(splitted) == 1 and splitted[0].lower() == 'yesterday':
        date = TODAY - relativedelta(days=1)
        return str(date.isoformat())
    elif splitted[1].lower() in ['sec', 'seconds', 'second', "secs"]:
        date = datetime.datetime.now() - relativedelta(seconds=int(splitted[0]))
        return str(date.date().isoformat())
    elif splitted[1].lower() in ['mins', 'minutes', 'min', "minute"]:
        date = datetime.datetime.now() - relativedelta(minutes=int(splitted[0]))
        return str(date.date().isoformat())
    elif splitted[1].lower() in ['hour', 'hours', 'hr', 'hrs', 'h']:
        date = datetime.datetime.now() - relativedelta(hours=int(splitted[0]))
        return str(date.date().isoformat())
    elif splitted[1].lower() in ['day', 'days', 'd']:
        date = TODAY - relativedelta(days=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['wk', 'wks', 'week', 'weeks', 'w']:
        date = TODAY - relativedelta(weeks=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['mon', 'mons', 'month', 'months', 'm']:
        date = TODAY - relativedelta(months=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['yrs', 'yr', 'years', 'year', 'y']:
        date = TODAY - relativedelta(years=int(splitted[0]))
        return str(date.isoformat())
    else:
        return "Wrong Argument format"


# import csv nltk is natural language toolkit
nltk.download('punkt')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

# googlenews = GoogleNews(start='09/09/2021', end='09/09/2021')
googlenews = GoogleNews(period='1h')

# query for google news
googlenews.search('cryptocurrency news')
result = googlenews.result()

# storing data to the dataframe

df = pd.DataFrame(result)

# traversing through pages of google news
for i in range(1, 35):
    googlenews.getpage(i)
    result = googlenews.result()
    df = pd.DataFrame(result)

list = []
for ind in df.index:
    dict = {}
    article = Article(df['link'][ind], config=config)
    data = article.download()
    try:
        article.parse()
        article.nlp()
        dict['pub_date'] = get_past_date(df['date'][ind])
        dict['source'] = df['media'][ind]
        dict['title'] = article.title
        dict['url'] = article.url
        dict['description'] = article.text
        dict['photo_url'] = article.top_image,
        dict['content'] =  "none"
        list.append(dict)
    except:
        pass
print(len(list))

news_df = pd.DataFrame(list)
news_df
news_df.to_csv("news3.csv", index=False)
