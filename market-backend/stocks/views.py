from django.http import JsonResponse
from django.views import View

from stocks.queries import stocks as stocks_queries


class Stocks(View):

    def get(self, request):
        stocks = stocks_queries.get_stocks()
        return JsonResponse(stocks, safe=False) 
