from .models import Order


class ProductForm(forms.ModelForm):
    """ Forms to handle products.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'video', 'weight', 'status', 'seller', 'address']


class OrderForm(forms.ModelForm):
    """Forms to handle orders.
    """
    class Meta:
        model = Order
        fields = ['product', 'buyer', 'order_name', 'quantity', 'order_description', 'delivery_date', 'status']


