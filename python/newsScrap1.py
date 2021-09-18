import requests
import pandas as pd
from datetime import date
import datetime
import readtime
from newspaper import Article
from newspaper import Config


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

today = date.today()

d1 = today.strftime("%Y-%m-%d")
url = 'https://newsapi.org/v2/everything?'

api_key = "441d1787a331477a858d7d9c0b07d4bb"

news_parameters = {
    'q': 'cryptocurrency',
    'page': '1',
    'pageSize': 100,
    'from': d1,
    'to': d1,
    'apiKey': '441d1787a331477a858d7d9c0b07d4bb',
    'language': 'en'
}
news = requests.get(url, params=news_parameters)
news = news.json()

news_articles = news["articles"]


def get_articles(file):
    article_results = []

    for i in range(len(file)):
        article_dict = {'title': file[i]['title'], 'source': file[i]['source'], 'description': file[i]['description'],
                        'pub_date': file[i]['publishedAt'], 'url': file[i]["url"],
                        'photo_url': file[i]['urlToImage']}

        article_results.append(article_dict)
    return article_results


news_df = pd.DataFrame(get_articles(news_articles))


def source_getter(df):
    source = []
    for source_dict in df['source']:
        source.append(source_dict['name'])

    df['source'] = source


def get_article_estimate_time(df):
    estimated_time = []
    summary = []
    for url1 in df['url']:
        article = Article(url1, config=config)
        try:
            article.download()
            article.parse()
            article.nlp()
            result = readtime.of_text(article.text)
            estimated_time.append(result.text)
            summary.append(article.summary)
        except:
            estimated_time.append("unknown")
            summary.append("unknown")
            pass

    df['read_time'] = estimated_time
    df['summary'] = summary


get_article_estimate_time(news_df)
source_getter(news_df)
news_df['pub_date'] = pd.to_datetime(
    news_df['pub_date']).apply(lambda x: x.date())

news_df.to_csv('news1.csv', index=False)
