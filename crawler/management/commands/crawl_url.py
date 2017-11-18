from django.core.management.base import BaseCommand

from hackeps import tasks


class Command(BaseCommand):

    help = 'Encolar url para el crawler'

    def add_arguments(self, parser):
        parser.add_argument(
            'service', type=str, help='Service name: instagram')
        parser.add_argument(
            'urls', nargs='+', type=str, help='List of urls to download')

    def handle(self, *args, **options):
        tasks.crawl_urls(options['service'], options['urls'])
