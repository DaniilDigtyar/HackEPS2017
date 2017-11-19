""" Factories para los profiles y los followers

    Actualmente solo esta implementado para instagram
"""
import logging

from scrapy.crawler import CrawlerProcess

from crawler import models
from . import profile, followers


logger = logging.getLogger(__name__)


class DownloaderException(Exception):
    pass


def get_profile(service, username):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    })

    klass = get_profile_class(service)
    process.crawl(klass, username=username)
    process.start()


def get_profile_class(service_name):
    """ Factory for profile module """
    if 'instagram' == service_name:
        return profile.InstagramProfile
    raise DownloaderException('Invalid service `{}`'.format(service_name))


def get_followers(service, username):
    """ Follower module entry point """
    try:
        # Ensure user exists
        user = models.User.objects.get(username__iexact=username)
    except models.User.DoesNotExist:
        # Cancel task
        logger.info('User `{}` does not exist'.format(username))
        return

    if user.scraped:
        logger.info('User `{}` already scraped'.format(username))
        return

    num_followers = user.followers
    klass = get_follower_class(service)
    klass.find(username, num_followers)
    user.scraped = True
    user.save()


def get_follower_class(service_name):
    """ Factory for followers module """
    if 'instagram' == service_name:
        return followers.InstagramFollowers()
    raise DownloaderException('Invalid service `{}`'.format(service_name))
