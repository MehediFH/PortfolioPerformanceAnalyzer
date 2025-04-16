from django.db import models

# Create your models here.
class Fund(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    one_year_return = models.FloatField()
    expense_ratio = models.FloatField()
    risk_level = models.CharField(max_length=20)

class Holding(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    shares = models.IntegerField()


