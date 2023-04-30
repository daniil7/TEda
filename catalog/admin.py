from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User
admin.site.site_header = "T.Еда Административная панель"


class DishesAdmin(admin.ModelAdmin):
    list_display = ("title","price","description","weight")

class Dish_CategoryAdminAdmin(admin.ModelAdmin):
    list_display = ("dish","category")

admin.site.register(Dishes, DishesAdmin)
admin.site.register(Dish_Category, Dish_CategoryAdminAdmin)

admin.site.register(Categories)


admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
