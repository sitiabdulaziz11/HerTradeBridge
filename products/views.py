from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

from .models import Product
from .forms import ProductForm

# List products
def all_products(request):
    """ To List all products.
    """
    products = Product.objects.all()
    
    for p in products:
        print(p.name, p.image)
        
    return render(request, 'products/all_products.html', {
        'products': products,
        })

# Add product
def add_product(request):
    """To add new products.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_pro')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {
        'form': form,
        })

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
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


def product_detail(request, pk):
    """To get all detail info of a product.
    """
    try:
        product_detl = Product.objects.get(pk=pk)
        return render(request, 'products/prod_detail.html', {
            "product_detl": product_detl,
        })
    except Product.DoesNotExist:
        print("product dosenot exist")

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'products/prod_detail.html', {
#         'products': products
#         })



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



