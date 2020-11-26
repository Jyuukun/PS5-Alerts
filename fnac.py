# -*- coding: utf-8 -*-

from weboob.browser.filters.standard import CleanText
from weboob.browser.url import URL

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//a[contains(@class, "Article-title")]'
    SEARCH_FILTERS = ('console', 'ps5', 'standard',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//div[contains(@class, "f-buyBox-availability")]'
    AVAILABLE_TEXTS = ('en stock en ligne', 'livrable en magasin',)

    @property
    def is_available(self):
        for div in self.doc.xpath(self.AVAILABILITY_XPATH):
            text = CleanText('.')(div)
            if any(available_text.lower() in text for available_text in self.AVAILABLE_TEXTS):
                return True


class FnacBrowser(GenericBrowser):
    BASEURL = 'https://www.fnac.com'

    SEARCH_PARAMS = {'Search': 'playstation 5'}
    DEFAULT_LINK = '/Console-Sony-PS5-Edition-Standard/a14119956/'

    results = URL('/SearchResult/ResultList.aspx', ResultsPage)
    article = URL('/', ArticlePage)
