import django_rq

from crawler import downloader


def crawl_urls(service_name, urls):
    queue = django_rq.get_queue('crawl')
    queue.enqueue(downloader.run, service_name, urls)
