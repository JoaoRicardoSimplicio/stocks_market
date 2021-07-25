from datetime import datetime

from stocks.models import Price, Stocks

from stocks.queries.stocks import save_stock


def _parser_stock(stock : dict) -> dict:
    stock['price'] = float(stock['price'].replace(',', '.'))
    stock['extraction_datetime'] = datetime(int(stock['year']), int(stock['month']), int(stock['day']),
                                            int(stock['hour']), int(stock['minute']), int(stock['second']), 0)
    return stock


def save_new_stock_price(stock : dict) -> None:
    stock = _parser_stock(stock)
    stock_record_db = save_stock(stock)
    Price.objects.create(stock=stock_record_db, price=stock['price'],
                         extraction_datetime=stock['extraction_datetime'])


def save_stocks_price(stocks : list) -> None:
    for stock in stocks:
        try:
            save_new_stock_price(stock)
        except Exception:
            raise(Exception)
