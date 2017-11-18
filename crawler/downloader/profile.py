import json
import re

from django.conf import settings
import scrapy

from crawler import models
from hackeps import tasks


class InstagramProfile(scrapy.Spider):

    name = "instagram_profile"

    def __init__(self, username, *args, **kwargs):
        super(InstagramProfile, self).__init__(*args, **kwargs)
        self.start_urls = ['https://instagram.com/{}/'.format(username), ]

    def parse(self, response):
        """ Download an instagram profile page and store the output """
        # Download the website JSON state
        json_string = response.xpath('//script/text()').re(
            r'sharedData = (.+);')[0]
        data = json.loads(json_string)
        user = self._store_profile(data)
        self._store_photos(user, data)
        tasks.crawl_followers('instagram', user.username)

    def _store_profile(self, data):
        try:
            # Get user data
            profile = data['entry_data']['ProfilePage'][0]['user']

            user = models.User.objects.get(username=profile['username'])
            user.followers = int(profile['followed_by']['count'])
            user.follows = int(profile['follows']['count'])
            user.description = profile['biography']
            user.profile_pic_link = profile['profile_pic_url']
            user.crawler = 'instagram'
            user.external_link = profile['id']
            user.parsed = True
        except Exception as e:
            # TODO: handle exception
            raise

        user.save()
        return user

    def _store_photos(self, user, data):
        profile = data['entry_data']['ProfilePage'][0]['user']

        hashtag_pattern = re.compile('#\w+')
        for node in profile['media'].get('nodes', []):
            hashtags = ', '.join(
                list(hashtag_pattern.findall(node['caption'])))
            photo = models.Photos(
                owner=user,
                likes=int(node['likes']['count']),
                comments=int(node['comments']['count']),
                hashtags=hashtags)
            photo.save()
