import django_rq

from crawler import downloader, models


def crawl_profiles(service_name, usernames):
    queue = django_rq.get_queue('profiles')
    for username in usernames:
        try:
            # If the user exists, do not crawl the profile
            user = models.User.objects.get(username__iexact=username)
        except models.User.DoesNotExist:
            user = models.User(username=username)
            user.save()
        if not user.parsed:
            queue.enqueue(
                downloader.get_profile, service_name, username)


def crawl_followers(service_name, username):
    queue = django_rq.get_queue('followers')
    queue.enqueue(downloader.get_followers, service_name, username)
