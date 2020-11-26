# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//h2/a'
    SEARCH_FILTERS = ('playstation', 'standard',)
    SEARCH_NOT_FILTERS = ('indisponible',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//div[@id="availability"]/span'


class AmazonBrowser(GenericBrowser):
    BASEURL = 'https://www.amazon.fr'
    
    SEARCH_PARAMS = {'k': "playstation 5"}
    DEFAULT_LINK = '/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/'

    results = URL('/s', ResultsPage)
    article = URL('/PlayStation', ArticlePage)
