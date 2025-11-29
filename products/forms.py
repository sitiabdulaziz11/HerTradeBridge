from django import forms

from .models import Order, Product


class ProductForm(forms.ModelForm):
    """ Forms to handle products.
    """
    class Meta:
        model = Product
        fields = ['name', 'price', 'amount', 'status', 'seller', 'address', 'description',  'image', 'video']


class OrderForm(forms.ModelForm):
    """Forms to handle orders.
    """
    class Meta:
        model = Order
        fields = ['product', 'buyer', 'order_name', 'quantity', 'order_description', 'delivery_date', 'status']


