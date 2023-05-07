from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

admin.site.site_header = "T.Еда Административная панель"

class DishInline(admin.StackedInline):
    model = Dish_Category
    extra = 3
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishInline]
    list_display = ["title", "image"]

class DishAdmin(admin.ModelAdmin):
    list_display = ["title",  "price", "thumbnail_tag"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
