
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('all_users/', views.all_users, name='all_users'),
    path('add_user/', views.add_user, name='add_ur'),
    path('addresses/', views.all_addresses, name='all_addresses'),
    path('reviews/', views.all_reviews, name='all_reviews'),
    path('purchase-history/', views.all_purchase_history, name='all_purchase_history'),
]
