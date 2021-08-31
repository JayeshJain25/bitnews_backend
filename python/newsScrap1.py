import requests 
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import numpy as np
from datetime import date
import datetime

today = date.today()

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=3)
Previous_Date_Formatted = Previous_Date.strftime ("%Y-%m-%d")

d1 = today.strftime("%Y-%m-%d")

url = 'https://newsapi.org/v2/everything?'

api_key = "441d1787a331477a858d7d9c0b07d4bb"

news_parameters = {
    'q': 'cryptocurrency',
    'page': '1',
    'pageSize': 100,
    'from': Previous_Date_Formatted,
    'to': d1,
    'apiKey': '441d1787a331477a858d7d9c0b07d4bb',
    'language': 'en'
}
news = requests.get(url, params=news_parameters)
news = news.json()

news_articles = news["articles"]
news_articles


def get_articles(file):
    article_results = []

    for i in range(len(file)):
        article_dict = {}
        article_dict['title'] = file[i]['title']
        article_dict['source'] = file[i]['source']
        article_dict['description'] = file[i]['description']
        article_dict['content'] = file[i]['content']
        article_dict['pub_date'] = file[i]['publishedAt']
        article_dict['url'] = file[i]["url"]
        article_dict['photo_url'] = file[i]['urlToImage']

        article_results.append(article_dict)
    return article_results


news_df = pd.DataFrame(get_articles(news_articles))


def source_getter(df):

    source = []
    for source_dict in df['source']:
        source.append(source_dict['name'])

    df['source'] = source


source_getter(news_df)
news_df['pub_date'] = pd.to_datetime(
    news_df['pub_date']).apply(lambda x: x.date())

news_df.to_csv('news1.csv', index=False)