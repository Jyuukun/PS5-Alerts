# -*- coding: utf-8 -*-

import logging
import os
import sys
import signal
import smtplib
import tempfile
import time

from configparser import ConfigParser

from weboob.tools.log import createColoredFormatter, getLogger

from amazon import AmazonBrowser
from auchan import AuchanBrowser
from boulanger import BoulangerBrowser
from cdiscount import CdiscountBrowser
from carrefour import CarrefourBrowser
from cultura import CulturaBrowser
from darty import DartyBrowser
from fnac import FnacBrowser
from leclerc import LeclercBrowser
from micromania import MicromaniaBrowser


def get_config():
    config = ConfigParser()
    config.read(os.path.dirname(os.path.abspath(sys.argv[0])) + '/config')
    return config


def send_mail(subject, text):
    config = get_config()

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(
                self.config['mail']['login'], self.config['mail']['password']
            )

            message = 'Subject: {}\n\n{}'.format(subject, text)
            server.sendmail(
                self.config['mail']['sender'], self.config['mail']['receiver'],
                message.encode('utf-8')
            )
    except Exception as e:
        logger = getLogger('send-mail')
        logger.error("Something went wrong while sending mail : %s" % str(e))


def create_colored_handler():
    # stderr logger
    format = '%(asctime)s:%(levelname)s:%(lineno)d:%(funcName)s %(message)s'
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(createColoredFormatter(sys.stderr, format))
    return handler


def signal_handler(signal, frame):
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)

    # create colored logger
    logging.root.setLevel(logging.DEBUG)
    logging.root.addHandler(create_colored_handler())
    logger = getLogger('ps5-availability')

    # create temporary directory
    responses_dirname = tempfile.mkdtemp(prefix='ps5_availability_session_')
    logger.info('Debug data will be saved in this directory: %s' % responses_dirname)

    browsers = (
        AmazonBrowser, AuchanBrowser, BoulangerBrowser, CarrefourBrowser, CdiscountBrowser,
        CulturaBrowser, DartyBrowser, FnacBrowser, LeclercBrowser, MicromaniaBrowser,
    )
    while True:
        waiting_time = 60 * 30

        for browser in browsers:
            browser = browser(logger=logger, responses_dirname=responses_dirname)
            logger.warning("Now trying on %s" % browser.BASEURL)

            try:
                is_available = browser.is_available
            except Exception as e:
                logger.error("Something went wrong : %s" % str(e))
                continue

            if is_available:
                logger.warning("Playstation 5 is AVAILABLE !!")
                send_mail(
                    "Playstation 5 Available !",
                    "Vite mec ! La PS5 est disponible sur %s ! Va dépenser toute ta tune ! :')" % browser.BASEURL
                )
                # we found one, no need to check to much now
                waiting_time = 60 * 60
                break
            else:
                logger.warning("Playstation 5 is not available on %s, so sad. :(" % browser.BASEURL)
        else:
            logger.critical("No PS5 found on any providers")

        logger.critical("waiting %s seconds to check again" % waiting_time)
        time.sleep(waiting_time)


if __name__ == '__main__':
    main()
