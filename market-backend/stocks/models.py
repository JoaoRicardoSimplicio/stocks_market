from django.db import models


class Stocks(models.Model):

    code = models.CharField(max_length=10, unique=True, null=False)


class Price(models.Model):
    
    stock = models.ForeignKey(
        Stocks,
        on_delete=models.CASCADE,
        null=False
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    extraction_datetime = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        unique_together = ('stock', 'extraction_datetime')
