from typing import Any, Dict
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.views import View
from catalog.models import Category, Dish
from .forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect

from catalog.services import cart

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
    for dish in dishes:
        dish.count = cart.dish_count(request.user, dish)
    return render(
            request,
            'category.html',
            context={
                'categories': categories,
                'dishes': dishes,
                }
            )

# Cart management

class PlusToCart(View):
    def post(self, request):
        dish_id = request.POST.get('dish_id', 0)
        dish = get_object_or_404(Dish, id=dish_id)
        cart.plus_to_cart(request.user, dish)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class MinusToCart(View):
    def post(self, request):
        dish_id = request.POST.get('dish_id', 0)
        dish = get_object_or_404(Dish, id=dish_id)
        cart.minus_to_cart(request.user, dish)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class RemoveFromCart(View):
    def post(self, request):
        dish_id = request.POST.get('dish_id', 0)
        dish = get_object_or_404(Dish, id=dish_id)
        cart.remove_from_cart(request.user, dish)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Registration

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
