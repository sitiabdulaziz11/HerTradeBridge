from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# List products
def all_products(request):
    products = Product.objects.all()
    return render(request, 'product/all_products.html', {'products': products})

# Add product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})

# Edit product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/edit_product.html', {'form': form, 'product': product})

# Delete product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('all_products')
    return render(request, 'product/delete_product.html', {'product': product})

# List orders
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'product/all_orders.html', {'orders': orders})

# Add order
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_orders')
    else:
        form = OrderForm()
    return render(request, 'product/add_order.html', {'form': form})

# Edit order
def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('all_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'product/edit_order.html', {'form': form, 'order': order})

# Delete order
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('all_orders')
    return render(request, 'product/delete_order.html', {'order': order})
    