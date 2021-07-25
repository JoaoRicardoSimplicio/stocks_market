from stocks.crawlers import info_money_crawler

from stocks.queries import prices


def update_stocks_price() -> list:
    stocks = info_money_crawler.execute()
    prices.save_stocks_price(stocks)
