import os

from django.conf import settings
import scrapy


class InstagramDownloader(scrapy.Spider):

    name = "instagram_downloader"

    def __init__(self, urls, *args, **kwargs):
        super(InstagramDownloader, self).__init__(*args, **kwargs)
        self.start_urls = urls

    def parse(self, response):
        """ Download an instagram page and store the output """
        # setup download dir
        os.makedirs(settings.CRAWLER_DOWNLOAD_PATH)

        # Get name from the url and set a filename
        page_name = self._get_name_by_url(response.url)
        filename = os.path.join(
            settings.CRAWLER_DOWNLOAD_PATH,
            'instagram_{}.json'.format(page_name))

        # Download the website state
        json_string = response.xpath('//script/text()').re(
            r'sharedData = (.+);')[0]

        # Store the contents
        with open(filename, 'w') as fd:
            fd.write(json_string)

    def _get_name_by_url(self, url):
        """ get the user name by url """
        return os.path.join(url, '').split("/")[-2]
