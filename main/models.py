from django.db import models


class Order(models.Model):
    sheet_id = models.CharField(max_length=30)
    price_dollars = models.IntegerField()
    price_rub = models.DecimalField(max_digits=20, decimal_places=2)
    delivery_date = models.DateField()
