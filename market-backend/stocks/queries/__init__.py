from stocks.models import Stocks


def _serializer_stocks_from_db(stocks : Stocks) -> list:
    # return [{"code": stock.code, "lasts_price": stock.price_set.last().price.to_eng_string()} for stock in stocks]
    result = {}
    for stock in stocks:
        result[stock.code] = [{price.extraction_datetime.strftime("%d-%m-%Y - %H:%M:%S"): price.price.to_eng_string()}
                              for price in stock.price_set.all().order_by('-extraction_datetime')[:5]]
    return result
