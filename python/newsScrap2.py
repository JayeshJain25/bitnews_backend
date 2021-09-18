from gnews import GNews
import pandas as pd
from datetime import datetime
import readtime
from newspaper import Article
from newspaper import Config

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

google_news = GNews(language='en', period='1h', max_results=100)
json_resp = google_news.get_news('cryptocurrency')
df = pd.DataFrame(json_resp)
list1 = []
for item in df.index:
    article = Article(df['url'][item], config=config)

    try:
        full_article = google_news.get_full_article(df['url'][item])
        article.download()
        article.parse()
        article.nlp()
        imageList = full_article.top_image
        dict = {'title': df['title'][item], 'description': full_article.text, 'url': df['url'][item],
                'pub_date': datetime.strptime(df['published date'][item], "%a, %d %b %Y %I:%M:%S %Z").date(),
                'source': df['publisher'][item]['title'], 'photo_url': imageList, 'summary': article.summary,
                'read_time': readtime.of_text(full_article.text)
                }

        list1.append(dict)
    except:
        pass

news_df = pd.DataFrame(list1)
news_df
news_df.to_csv("news2.csv", index=False)
