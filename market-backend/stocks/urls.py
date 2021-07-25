from django.urls import path

from stocks.views import Stocks


app_name = 'stocks'


urlpatterns = [
    path('', Stocks.as_view(), name='stocks_view'),
]
