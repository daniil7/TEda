from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(blank=True, null=True)
    status = models.IntegerField()

    dishes = models.ManyToManyField('Dish', through='Order_Dish')


class Dish(models.Model):
    title = models.CharField(max_length=500, verbose_name = "Блюдо")
    price = models.PositiveIntegerField(verbose_name = "Цена")
    description = models.CharField(max_length=500, verbose_name = "Описание", blank=True, null=True)
    image = models.ImageField(verbose_name = "Фотография", blank=True, null=True)
    weight = models.PositiveIntegerField(verbose_name = "Вес", blank=True, null=True)

    categories = models.ManyToManyField('Category', through='Dish_Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категория блюд")

    dishes = models.ManyToManyField('Dish', through='Dish_Category')

    def __str__(self):
        return str(self.title) or ""

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Order_Dish(models.Model):
    order =  models.ForeignKey('Order', on_delete=models.CASCADE)
    dish =  models.ForeignKey('Dish', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)


class Dish_Category(models.Model):
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "блюдо"
        verbose_name_plural = "блюда данной категории"
