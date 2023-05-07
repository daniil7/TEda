from django.shortcuts import render

from catalog.models import Category

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
