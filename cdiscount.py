# -*- coding: utf-8 -*-

from weboob.browser.filters.standard import CleanText, Regexp
from weboob.browser.url import URL
from weboob.browser.pages import HTMLPage

from generic import (
    GenericResultsPage, GenericArticlePage, GenericBrowser
)


class CookieJsPage(HTMLPage):
    def get_js_cookie(self):
        return Regexp(
            CleanText('//script[contains(text(), "document.cookie")]'),
            r'document.cookie=\"js=(.*?);',
        )(self.doc)


class ResultsPage(GenericResultsPage):
    LINKS_XPATH = '//li[has-class("crItem")]//a'
    SEARCH_FILTERS = ('ps5', 'console',)


class ArticlePage(GenericArticlePage):
    AVAILABILITY_XPATH = '//input[@type="submit"]/@value'
    AVAILABLE_TEXTS = ('ajouter au panier',)


class CdiscountBrowser(GenericBrowser):
    BASEURL = 'https://www.cdiscount.com'

    js_cookie = URL(r'/$', CookieJsPage)
    results = URL('/jeux-pc-video-console/ps5/console-ps5/l-1035001.html', ResultsPage)
    article = URL('/', ArticlePage)


    def search_link(self):
        # this part of the code is to simulate the activation of javascript
        # if we do not change the user-agent we are still blocked
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:80.0) Gecko/20100101 Firefox/80.0'
        self.js_cookie.go()
        cookie = self.page.get_js_cookie()
        self.session.cookies.set('js', cookie)

        return super(CdiscountBrowser, self).search_link()
