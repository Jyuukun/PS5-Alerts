# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//div[has-class("product-name")]/a[contains(@data-gtm, "499.99")]'
    SEARCH_FILTERS = ('playstation',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//div[has-class("prices-add-to-cart-actions")]//button[not(@disabled)]'
    AVAILABLE_TEXTS = ('ajouter au panier',)


class MicromaniaBrowser(GenericBrowser):
    BASEURL = 'https://www.micromania.fr'
    
    DEFAULT_LINK = '/playstation-5-105642.html'

    results = URL('/produits-playstation5.html', ResultsPage)
    article = URL('/', ArticlePage)
