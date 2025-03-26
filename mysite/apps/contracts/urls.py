from django.urls import path
from .views import (
    ContractListView,
    ContractDetailView,
    ContractCreateView,
    ContractUpdateView,
    ContractDeleteView,
)

app_name = 'contracts'


urlpatterns = [
    path('', ContractListView.as_view(), name='contract_list'),
    path('new/', ContractCreateView.as_view(), name='contract_create'),
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_update'),
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
]
