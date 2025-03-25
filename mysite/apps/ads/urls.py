from django.urls import path
from . import views

app_name = "ads"

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('new/', views.advertisement_create, name='advertisement_create'),
    path('<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('<int:pk>/edit/', views.advertisement_update, name='advertisement_update'),
    path('<int:pk>/delete/', views.advertisement_delete, name='advertisement_delete'),
    path('statistic/', views.advertisement_statistic, name='advertisement_statistic'),
]
