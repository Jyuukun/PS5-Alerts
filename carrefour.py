# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//a[has-class("product-card-title")]'
    SEARCH_FILTERS = ('ps5', 'standard',)
    SEARCH_NOT_FILTERS = ('digital',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//div[@id="data-produit-acheter"]'
    AVAILABLE_TEXTS = ('acheter',)


class CarrefourBrowser(GenericBrowser):
    BASEURL = 'https://www.carrefour.fr'
    
    SEARCH_PARAMS = {'q': "playstation 5"}
    DEFAULT_LINK = 'https://reservation.carrefour.fr/produit/playstation-5/ps5-edition-standard'

    results = URL('/s', '/jeux', ResultsPage)
    article = URL('/p', 'https://reservation.carrefour.fr/produit', ArticlePage)
