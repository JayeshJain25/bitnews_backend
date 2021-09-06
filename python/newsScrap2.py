from gnews import GNews
import pandas as pd
from datetime import datetime

google_news = GNews(language='en', period='1h', max_results=100)
json_resp = google_news.get_news('cryptocurrency')
df = pd.DataFrame(json_resp)
list1 = []
for item in df.index:
    try:
        full_article = google_news.get_full_article(df['url'][item])
        imageList = full_article.top_image

        dict = {'title': df['title'][item], 'description': full_article.text, 'url': df['url'][item],
                'pub_date':  datetime.strptime(df['published date'][item], "%a, %d %b %Y %I:%M:%S %Z").date(),
                'source': df['publisher'][item]['title'], 'photo_url': imageList, 'content': "none"
                }

        list1.append(dict)
    except:
        pass

news_df = pd.DataFrame(list1)
news_df
news_df.to_csv("news2.csv", index=False)
