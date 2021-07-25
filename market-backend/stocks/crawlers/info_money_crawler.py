import requests

from datetime import datetime

from bs4 import BeautifulSoup


INFO_MONEY_BOVESPA_URL = "https://www.infomoney.com.br/cotacoes/ibovespa/"


def _get_info_money_page_stocks(url : str = INFO_MONEY_BOVESPA_URL) -> str:
    return requests.get(url)


def _extract_stocks_from_info_money_page() -> dict:
    date_now = datetime.now()
    content_page = _get_info_money_page_stocks().content
    html_soup = BeautifulSoup(content_page, "html.parser")
    stocks_table = html_soup.find('table', id='high').find_all("tr")
    stocks_table += html_soup.find("table", id="low").find_all("tr")
    stocks = [{"code": stock.find_all("td")[0].text, 
              "price": stock.find_all("td")[1].text,
              "day_variation": stock.find_all("td")[2].text,
              "day": date_now.day,
              "month": date_now.month,
              "year": date_now.year,
              "hour": date_now.hour,
              "minute": date_now.minute,
              "second": date_now.second}
            for stock in stocks_table if stock.find_all("td")]
    return stocks


def execute() -> list:
    stocks = sorted(_extract_stocks_from_info_money_page(), key=lambda stock: stock["day_variation"], reverse=True)
    return stocks


if __name__ == "__main__":
   execute() 
