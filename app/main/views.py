from flask import render_template,request,redirect,url_for
from . import main
from ..models import News
from ..request import get_news, get_articles, headlines

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting popular news
    popular_news = get_news('general')
    business_news = get_news('business')
    sports_news = get_news('sports')
    health_news = get_news('health')
    ent_news = get_news('entertainment')
    tech_news = get_news('technology')
    print(popular_news)
    title = 'Home - Welcome to The best News Website Online'

    # message = 'Hello World'
    return render_template('index.html', title = title, general = popular_news, business = business_news, sports = sports_news,health = health_news, entertainment = ent_news, technology = tech_news, name = 'News Highlights')

@main.route('/news/<source_id>&<int:per_page>')
def news_articles(source_id,per_page):

    '''
    View movie page function that returns the movie details page and its data
    '''

    title = 'Headlines'

    news_source = get_articles(source_id,per_page)

    return render_template('news.html', name = source_id,title=title, news = news_source)

@main.route('/headlines&<int:per_page>')
def news_headlines(per_page):

    in_the_headlines = headlines(per_page)
    title = 'Top headlines'
    return render_template('headlines.html', title=title, name='Headlines',news=in_the_headlines)