# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//div[@class="designations"]/h2/a'
    SEARCH_FILTERS = ('console', 'ps5', 'standard',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = """
        //div[@class="informations"]//div[has-class("onlinePurchase") and has-class("on")]/a
    """
    AVAILABLE_TEXTS = ('ajouter au panier',)


class BoulangerBrowser(GenericBrowser):
    BASEURL = 'https://www.boulanger.com'
    
    SEARCH_PARAMS = {'tr': 'playstation 5'}
    DEFAULT_LINK = '/ref/1147567'

    results = URL('/resultats', '/c', ResultsPage)
    article = URL('/ref', ArticlePage)
