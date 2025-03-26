from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    AdvertisementDeleteView,
    AdvertisementStatisticView
)

app_name = 'ads'


urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('new/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('<int:pk>/edit/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),
    path('statistic/', AdvertisementStatisticView.as_view(), name='advertisement_statistic'),
]
