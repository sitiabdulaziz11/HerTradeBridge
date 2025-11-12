
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_pro'),
    path('add_products/', views.add_product, name='add_pro'),
    path('product_detl/<int:pk>/', views.product_detail, name='pro_detl'),
    path('orders/', views.all_orders, name='all_orders'),
]
