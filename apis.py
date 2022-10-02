import window
from newsapi import NewsApiClient
import multiprocessing
apikey = 'e57b00e4bf54487892765f153c215924'


# Init
newsapi = NewsApiClient(api_key=apikey)
win=window.Window()

def headlines():
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(language='en', country='in')
    multiprocessing.Process(target=win.disp_article, args=(top_headlines['articles'],)).start()
    # return top_headlines['articles']



def news_on(topic):
    # # /v2/everything
    all_articles = newsapi.get_everything(q=topic,
                                          qintitle=topic,
                                          language='en',
                                          sort_by='relevancy')
                                          
    return all_articles


# print(news_on('bitcoins'))
# print(headlines())
