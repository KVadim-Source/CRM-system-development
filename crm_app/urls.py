from django.urls import path
import views


urlpatterns = [
    path('create_roles/', views.create_roles, name='create_roles'),
    path('assign_role/<str:role_name>/', views.assign_role, name='assign_role'),

    path('services/', views.services_list, name='services_list'),
    path('services/create/', views.create_service, name='create_service'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/<int:pk>/edit/', views.edit_service, name='edit_service'),
    path('services/<int:pk>/delete/', views.delete_service, name='delete_service'),

    path('ad_campaigns/', views.ad_campaigns_list, name='ad_campaigns_list'),
    path('ad_campaigns/create/', views.create_ad_campaign, name='create_ad_campaign'),

    path('potential_clients/', views.potential_clients_list, name='potential_clients_list'),
    path('potential_clients/create/', views.create_potential_client, name='create_potential_client'),
    path('potential_clients/<int:pk>/convert/', views.convert_to_active_client, name='convert_to_active_client'),
    path('potential_clients/<int:pk>/create_active/', views.create_active_client, name='create_active_client_from_potential'),

    path('contracts/', views.contracts_list, name='contracts_list'),
    path('contracts/create/', views.create_contract, name='create_contract'),
    path('contracts/<int:pk>/', views.contract_detail, name='contract_detail'),
    path('contracts/<int:pk>/edit/', views.edit_contract, name='edit_contract'),
    path('contracts/<int:pk>/delete/', views.delete_contract, name='delete_contract'),

    path('active_clients/', views.active_clients_list, name='active_clients_list'),
    path('active_clients/create/<int:pk>/', views.create_active_client, name='create_active_client'),
    path('active_clients/<int:pk>/', views.active_client_detail, name='active_client_detail'),
    path('active_clients/<int:pk>/edit/', views.edit_active_client, name='edit_active_client'),
    path('active_clients/<int:pk>/delete/', views.delete_active_client, name='delete_active_client'),

    path('ad_campaign_stats/', views.ad_campaign_stats, name='ad_campaign_stats'),
    path('ad_campaigns/<int:pk>/', views.ad_campaign_detail, name='ad_campaign_detail'),
    path('ad_campaigns/<int:pk>/edit/', views.edit_ad_campaign, name='edit_ad_campaign'),
    path('ad_campaigns/<int:pk>/delete/', views.delete_ad_campaign, name='delete_ad_campaign'),
]
