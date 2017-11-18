from django.core.management.base import BaseCommand

from hackeps import tasks


class Command(BaseCommand):

    help = 'Encolar username para descargar los usuarios'

    def add_arguments(self, parser):
        parser.add_argument(
            'service', type=str, help='Service name: instagram')
        parser.add_argument(
            'username', type=str, help='Username to crawl the followers')

    def handle(self, *args, **options):
        tasks.crawl_followers(options['service'], options['username'])
