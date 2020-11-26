# -*- coding: utf-8 -*-

from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//div[contains(@class, "infos_container")]//a'
    SEARCH_FILTERS = ('ps5', 'standard',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//p[@class="delivery_date"]'


class DartyBrowser(GenericBrowser):
    BASEURL = 'https://www.darty.com'
    
    DEFAULT_LINK = '/nav/achat/informatique/ps4/consoles_ps4/sony_sony_ps5_standard.html'

    results = URL('/nav/recherche/playstation-5.html', ResultsPage)
    article = URL('/nav/achat', ArticlePage)
