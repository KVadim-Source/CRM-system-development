from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ),
         name='login'
         ),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('', views.index, name='index'),
]
