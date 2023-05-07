from django.shortcuts import render


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(
        request,
        'index.html',
        )

# Create your views here.
