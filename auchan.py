# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//div[contains(@class, "product-item")]/a[@title]'
    SEARCH_FILTERS = ('sony', 'standard',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//div[contains(@class,"inStoreAvailability")]'
    AVAILABLE_TEXTS = ('retrait',)


class AuchanBrowser(GenericBrowser):
    BASEURL = 'https://www.auchan.fr'
    
    SEARCH_PARAMS = {'text': 'playstation 5'}

    results = URL('/recherche', '/jeux-video', ResultsPage)
    article = URL('/', ArticlePage)
