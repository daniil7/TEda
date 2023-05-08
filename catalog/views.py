from django.shortcuts import render
from django.shortcuts import get_object_or_404

from catalog.models import Category, Dish

# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    categories = Category.objects.all()
    return render(
        request,
        'index.html',
        context={
            'categories': categories,
            }
        )

def index_category(request, category_id):
    """
    Функция отображения блюд конкретной категории
    """
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    dishes = Dish.objects.filter(categories=category)
    return render(
            request,
            'category.html',
            context={
                'categories': categories,
                'dishes': dishes,
                }
            )
