# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//div[@class="item"]//h3/a'
    SEARCH_FILTERS = ('playstation', 'console',)
    SEARCH_NOT_FILTERS = ('digital',)

    def is_here(self):
        return bool(self.doc.xpath(self.LINKS_XPATH))


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//p[has-class("availability")]'


class CulturaBrowser(GenericBrowser):
    BASEURL = 'https://www.cultura.com'
    
    SEARCH_PARAMS = {'q': "playstation", 'classification': "59885"}

    results = URL('/catalogsearch/result/', '/', ResultsPage)
    article = URL('/', ArticlePage)
