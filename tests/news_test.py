import unittest
from app.models import News
# News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('abc-news','ABC NEWS','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','http://www.abc.net.au/news','business','au')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    def test_init(self):
        self.assertEqual(self.new_news.id,'abc-news')
        self.assertEqual(self.new_news.name,'ABC NEWS')
        self.assertEqual(self.new_news.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEqual(self.new_news.url,'http://www.abc.net.au/news')
        self.assertEqual(self.new_news.country,'au')


# if __name__ == '__main__':
#     unittest.main()
