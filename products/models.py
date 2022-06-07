from itertools import product
from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Allergy(models.Model):
    name     = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'allergies'

class AllergyDrink(models.Model):
    name    = models.CharField(max_length=20)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergydrinks'