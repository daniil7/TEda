from profile import Profile
from django.db import models
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from catalog.models import Category, Dish
from .forms import UserCreationForm
from django.contrib.auth import authenticate,login  
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Profile
from django.contrib.auth.forms import UserChangeForm



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
            
        

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'
    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'profile/create_profile.html'
    fields = ['profile_pic', 'fio']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('profile')


class UserEditView(CreateView):
    form_class = UserChangeForm
    template_name = "profile/edit_profile.html"
    #success_url = reverse_lazy("")


