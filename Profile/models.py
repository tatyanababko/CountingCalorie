from django.db import models


class Products(models.Model):
    name_product = models.CharField(max_length=256, unique=True)
    proteins = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()


class UserProducts(models.Model):
    
