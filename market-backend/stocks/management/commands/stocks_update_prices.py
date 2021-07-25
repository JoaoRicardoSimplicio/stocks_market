from django.core.management.base import BaseCommand

from stocks.updaters.prices import update_stocks_price


class Command(BaseCommand):
    help = 'Update the price of all stocks in database'

    def handle(self, *args, **options):
        update_stocks_price()

