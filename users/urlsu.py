
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.all_users, name='all_users'),
    path('addresses/', views.all_addresses, name='all_addresses'),
    path('reviews/', views.all_reviews, name='all_reviews'),
    path('purchase-history/', views.all_purchase_history, name='all_purchase_history'),
]
