"""
URL configuration for teda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from catalog.views import ShowProfilePageView, CreateProfilePageView, UserEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='Profile'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name='create_user_profile'),
    path('user_edit/',CreateProfilePageView.as_view(), name='edit_profile'),

    path('catalog/', include('catalog.urls')),
    path('',include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
