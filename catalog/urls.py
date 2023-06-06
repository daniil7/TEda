from django.urls import path, include
from .views import *
from catalog import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),

    path('category/<int:category_id>/', views.index_category, name='index_category'),
    path('shoppingcart/', views.shopping_cart, name='shopping_cart'),

    # cart
    #
    path('cart/plus/', views.PlusToCart.as_view(), name='cart_plus'),
    path('cart/minus/', views.MinusToCart.as_view(), name='cart_minus'),
    path('cart/remove/', views.RemoveFromCart.as_view(), name='cart_remove'),
    path('cart/makeorder/', views.MakeOrder.as_view(), name='make_order'),

    # account
    #
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', views.RegisterUser.as_view(), name='register'),
    #path('login/', views.LoginUser),

    # api
    #
    path('api/', include('catalog.urls_api')),
]
