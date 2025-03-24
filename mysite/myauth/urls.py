from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index, name='index'),
]
