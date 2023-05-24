from django.urls import path, include
from .views import *
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),

    path('category/<int:category_id>/', views.index_category, name='index_category'),

    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', views.RegisterUser.as_view(), name='register'),

    #path('login/', views.LoginUser),

]
