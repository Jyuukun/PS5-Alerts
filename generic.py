# -*- coding: utf-8 -*-

from weboob.browser.browsers import PagesBrowser
from weboob.browser.exceptions import ServerError
from weboob.browser.filters.html import Link
from weboob.browser.filters.standard import CleanText
from weboob.browser.pages import HTMLPage
from weboob.browser.url import URL


class GenericResultsPage(HTMLPage):
    LINKS_XPATH = None
    SEARCH_FILTERS = tuple()
    SEARCH_NOT_FILTERS = tuple()

    def get_link(self):
        if not self.LINKS_XPATH:
            return

        links = self.doc.xpath(self.LINKS_XPATH)
        for link in links:
            title = CleanText('.')(link).lower()
            if (
                all(_filter.lower() in title for _filter in self.SEARCH_FILTERS)
                and all(_filter.lower() not in title for _filter in self.SEARCH_NOT_FILTERS)
            ):
                return Link('.')(link)

        if not links:
            self.logger.error("No elements found with %s" % self.LINKS_XPATH)


class GenericArticlePage(HTMLPage):
    AVAILABILITY_XPATH = None
    AVAILABLE_TEXTS = ('en stock',)

    @property
    def is_available(self):
        text = CleanText(self.AVAILABILITY_XPATH)(self.doc).lower()
        if any(available_text.lower() in text for available_text in self.AVAILABLE_TEXTS):
            return True


class GenericBrowser(PagesBrowser):
    BASEURL = ''

    SEARCH_PARAMS = {}
    DEFAULT_LINK = ''

    results = URL('/results', GenericResultsPage)
    article = URL('/article', GenericArticlePage)

    def search_link(self):
        self.results.go(params=self.SEARCH_PARAMS)

        if self.results.is_here():
            link = self.page.get_link()
        else:
            link = None

        if not link:
            self.logger.warning("No results found from search")

        return link

    @property
    def is_available(self):
        link = self.search_link()

        if link or self.DEFAULT_LINK:
            try:
                self.location(link or self.DEFAULT_LINK)
            except ServerError:
                self.location(self.DEFAULT_LINK)

            if not self.article.is_here():
                self.logger.error("Not on article page !")
            else:
                return self.page.is_available
