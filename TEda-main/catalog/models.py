from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Tokens(models.Model):
    token = models.CharField(max_length=100)
    

class Orders(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    time = models.TimeField()
    status = models.IntegerField()

class Order_Dish(models.Model):
    order =  models.ForeignKey('Orders', on_delete=models.PROTECT)
    dish =  models.ForeignKey('Dishes', on_delete=models.PROTECT)
    count = models.IntegerField()
    
 
class Dishes(models.Model):
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    weight = models.IntegerField()


class Dish_Category(models.Model):
    dish = models.ForeignKey('Dishes', on_delete=models.PROTECT)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)


class Categories(models.Model):
    title = models.CharField(max_length=100)