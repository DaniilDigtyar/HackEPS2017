from scrapy.crawler import CrawlerProcess

from . import instagram


class DownloaderException(Exception):
    pass


def run(service, urls):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    klass = get_downloader_class(service)
    process.crawl(klass, urls=urls)
    process.start()


def get_downloader_class(service_name):
    if 'instagram' == service_name:
        return instagram.InstagramDownloader
    raise DownloaderException('Invalid service `{}`'.format(service_name))
