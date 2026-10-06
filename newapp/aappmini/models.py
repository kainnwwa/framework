from django.db import models

class Manufacturer(models.Model):
    name = models.CharField()
    country = models.CharField()

class Product(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
