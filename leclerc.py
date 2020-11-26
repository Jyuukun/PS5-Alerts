# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//div[@class="article_box"]//a[@onclick]'
    SEARCH_FILTERS = ('console', 'playstation', 'standard',)

    def is_here(self):
        return bool(self.doc.xpath(self.LINKS_XPATH))


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//tr[@class="ProductBuyBox"]//span'


class LeclercBrowser(GenericBrowser):
    BASEURL = 'https://www.culture.leclerc'
    
    SEARCH_PARAMS = {'q': 'playstation 5', 'univers': "all"}
    DEFAULT_LINK = '/jeux-video-u/playstation-5-u/consoles-u/console-playstation-5---edition-standard-ps5-0711719395201-pr'

    results = URL('/pageRecherche', '/', ResultsPage)
    article = URL('/', ArticlePage)
