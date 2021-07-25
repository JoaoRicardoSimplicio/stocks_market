from django.db import IntegrityError

from stocks.models import Stocks
from stocks import queries


def save_stock(stock: dict) -> Stocks:
    stock_record_db, _ = Stocks.objects.get_or_create(code=stock['code'])
    return stock_record_db


def save_stocks(stocks: list) -> None:
    for stock in stocks:
        try:
            save_stock(stock)
        except IntegrityError:
            pass


def get_stocks(filter_expression : str = None) -> Stocks:
    stocks = Stocks.objects.all()
    if filter_expression:
        pass
    return queries._serializer_stocks_from_db(stocks)
