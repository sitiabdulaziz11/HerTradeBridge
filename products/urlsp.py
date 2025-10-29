
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('orders/', views.all_orders, name='all_orders'),
]
