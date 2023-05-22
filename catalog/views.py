from typing import Any, Dict
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.views import View
from catalog.models import Category, Dish
from .forms import UserCreationForm
from django.contrib.auth import authenticate,login  


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



class RegisterUser(View):
    teamplate_name = "registration/register.html"

    def get(self,request):
        context = {
            'form': UserCreationForm() 
        }
        return render(request,self.teamplate_name,context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if(form.is_valid()):
            form.save()
            UserName = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username =UserName, password = password )
            login(request, user)
            return redirect('/')
        context = {
                'form': form
            }
        return render(request, self.teamplate_name, context)
            
        