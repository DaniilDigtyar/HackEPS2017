from django.core.management.base import BaseCommand

from hackeps import tasks


class Command(BaseCommand):

    help = 'Encolar username para descargar el profile'

    def add_arguments(self, parser):
        parser.add_argument(
            'service', type=str, help='Service name: instagram')
        parser.add_argument(
            'username', nargs='+', type=str, help='List of usernames')

    def handle(self, *args, **options):
        tasks.crawl_profiles(options['service'], options['username'])
