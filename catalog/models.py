from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_init
from django.utils.html import format_html

import os

from catalog.services.create_thumbnail import createThumbnail


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
    image = models.ImageField(verbose_name = "Фотография", upload_to="dish-images/", blank=True, null=True)
    previous_image = None
    weight = models.PositiveIntegerField(verbose_name = "Вес", blank=True, null=True)

    categories = models.ManyToManyField('Category', through='Dish_Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def thumbnail_path(self):
        return os.path.join('dish-images/thumbnails', os.path.basename(self.image.name))
    def thumbnail_url(self):
        return os.path.join(settings.MEDIA_URL, self.thumbnail_path())
    def thumbnail_tag(self):
        return format_html('<img src="{0}">', self.thumbnail_url())
    thumbnail_tag.allow_tags = True
    thumbnail_tag.description = "Изображение"
    thumbnail_tag.short_description = "Изображение"

    def image_tag(self):
        return format_html('<img src="{0}">', self.image.url)
    image_tag.allow_tags = True
    image_tag.description = "Изображение"
    thumbnail_tag.short_description = "Изображение"

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        if (instance.previous_image != instance.image or created) and (instance.image.name is not None):
            if not created:
                os.remove(os.path.join(settings.MEDIA_ROOT, instance.previous_image.name))
                os.remove(os.path.join(settings.MEDIA_ROOT, "dish-images/thumbnails", os.path.basename(instance.previous_image.name)))
            thumbnail_directory = os.path.join(settings.MEDIA_ROOT, "dish-images/thumbnails")
            thumbnail_name = os.path.basename(instance.image.name)
            thumbnail = createThumbnail(os.path.join(settings.MEDIA_ROOT, instance.image.name))
            if not os.path.exists(thumbnail_directory):
                os.makedirs(thumbnail_directory)
            if thumbnail == False:
                return
            thumbnail.save(os.path.join(thumbnail_directory, thumbnail_name))

    @staticmethod
    def remember_state(sender, instance, **kwargs):
        instance.previous_image = instance.image

post_save.connect(Dish.post_save, sender=Dish)
post_init.connect(Dish.remember_state, sender=Dish)


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
