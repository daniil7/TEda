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
    title = models.CharField(max_length=500, verbose_name = "Блюдо")
    price = models.CharField(max_length=100, verbose_name = "Цена")
    description = models.CharField(max_length=500, verbose_name = "Описание")
    image = models.ImageField(verbose_name = "Фотография")
    weight = models.IntegerField(verbose_name = "Вес")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Dish_Category(models.Model):
    dish = models.ForeignKey('Dishes', on_delete=models.PROTECT,verbose_name="Блюдо")
    category = models.ForeignKey('Categories', on_delete=models.PROTECT,verbose_name="Категория блюда: ")
    def __str__(self):
        return str(self.category) or " "
    
    class Meta:
        verbose_name = "Категорию блюда"
        verbose_name_plural = "Категории блюд"


class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категория блюд")
    def __str__(self):
        return str(self.title) or ""
    
    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

#sadsad