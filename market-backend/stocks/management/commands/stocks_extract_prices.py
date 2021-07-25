from django.core.management.base import BaseCommand

from stocks.crawlers import info_money_crawler


class Command(BaseCommand):
    help = 'Extract the price of all shares that suffered price variation on the day'

    def handle(self, *args, **options):
       stocks = info_money_crawler.execute()
       for stock in stocks:
           print(stock)
