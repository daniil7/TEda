from django.urls import path, include
from .views import *
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),

    path('category/<int:category_id>/', views.index_category, name='index_category'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterUser.as_view()),
    #path('profile/', ###),
]
