from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib import messages

from catalog.models import Category, Dish, Order
from catalog.services import cart
from .forms import UserCreationForm

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

def shopping_cart(request):
    """
    Функция отображения корзины пользователя
    """
    categories = Category.objects.all()
    order = Order.objects.filter(user=request.user, status=Order.statuses.not_started).first()
    dishes = None
    total_sum = 0
    if order:
        dishes = order.dishes.all()
        for dish in dishes:
            dish.count = cart.dish_count(request.user, dish)
        total_sum = sum(dish.price * dish.count for dish in dishes)
    return render(
            request,
            'shopping-cart.html',
            context={
                'categories': categories,
                'dishes': dishes,
                'total_sum': total_sum,
                }
            )

# Cart management

class PlusToCart(View):
    """
    Обработка запроса добавления товара в корзину
    """
    def post(self, request):
        dish_id = request.POST.get('dish_id', 0)
        dish = get_object_or_404(Dish, id=dish_id)
        cart.plus_to_cart(request.user, dish)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class MinusToCart(View):
    """
    Обработка запроса удаления 1 позиции товара из корзины
    """
    def post(self, request):
        dish_id = request.POST.get('dish_id', 0)
        dish = get_object_or_404(Dish, id=dish_id)
        cart.minus_to_cart(request.user, dish)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class RemoveFromCart(View):
    """
    Обработка запроса полного удаления товара из корзины
    """
    def post(self, request):
        dish_id = request.POST.get('dish_id', 0)
        dish = get_object_or_404(Dish, id=dish_id)
        cart.remove_from_cart(request.user, dish)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class MakeOrder(View):
    """
    Оформление заказа
    """
    def post(self, request):
        try:
            cart.make_order(request.user)
        except cart.ObjectNotFoundError as exc:
            messages.error(request=request, message=exc.message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Registration

class RegisterUser(View):
    """
    Регистрация пользователя
    """
    teamplate_name = "registration/register.html"

    def get(self,request):
        context = {
            'form': UserCreationForm()
        }
        return render(request,self.teamplate_name,context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = user_name, password = password )
            login(request, user)
            return redirect('/')
        context = {
                'form': form
            }
        return render(request, self.teamplate_name, context)
