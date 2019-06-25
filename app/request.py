import urllib.request,json
from .models import News, Articles



# Getting api key
api_key = None

# Getting the movie base url
base_url = None
topheadlines_url = None
everythingsource_url = None

def configure_request(app):
    global api_key,base_url,topheadlines_url,everythingsource_url

    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    topheadlines_url = app.config["TOP_HEADLINES_BASE_URL"]
    everythingsource_url = app.config["EVERYTHING_SOURCE_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        if url:
            news_object = News(id,name,description,url,category,country)
            news_results.append(news_object)

    return news_results

def get_articles(source_id,limit):
    '''
    Function that gets articles based on the source id and we also limit the number of articles per page
    '''

    get_articles_url = everythingsource_url.format(source_id,limit,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            get_articles_list = get_articles_response['articles']
            articles_results = process_articles(get_articles_list)
    
    return articles_results

def process_articles(my_articles):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of movie objects
    '''
    articles_list = []
    for articles in my_articles:
        author = articles.get('author')
        title = articles.get('title')
        description = articles.get('description')
        url = articles.get('url')
        urlToImage = articles.get('urlToImage')
        publishedAt = articles.get('publishedAt')

        if urlToImage:
            articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
            articles_list.append(articles_object)

    return articles_list

def headlines(limit):

    get_headlines_url = topheadlines_url.format(limit,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)

        headlines_results = None

        if headlines_response['articles']:
            get_articles_list = headlines_response['articles']
            headlines_results = process_articles(get_articles_list)
        
    return headlines_results