from django.shortcuts import render

# Create your views here.

from .models import UserProfile
from .forms import UserProfileForm

# List users
def all_users(request):
    users = UserProfile.objects.all()
    return render(request, 'user/all_users.html', {'users': users})

# Add user (signup)
def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_users')
    else:
        form = UserProfileForm()
    return render(request, 'user/add_user.html', {'form': form})

# Edit user
def edit_user(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'user/edit_user.html', {'form': form, 'user': user})

# Delete user
def delete_user(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('all_users')
    return render(request, 'user/delete_user.html', {'user': user})

# List addresses
def all_addresses(request):
    addresses = Address.objects.all()
    return render(request, 'user/all_addresses.html', {'addresses': addresses})

# Add address
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_addresses')
    else:
        form = AddressForm()
    return render(request, 'user/add_address.html', {'form': form})

# Edit address
def edit_address(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('all_addresses')
    else:
        form = AddressForm(instance=address)
    return render(request, 'user/edit_address.html', {'form': form, 'address': address})

# Delete address
def delete_address(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('all_addresses')
    return render(request, 'user/delete_address.html', {'address': address})


# List reviews
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'user/all_reviews.html', {'reviews': reviews})

# Add review
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_reviews')
    else:
        form = ReviewForm()
    return render(request, 'user/add_review.html', {'form': form})

# Edit review
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('all_reviews')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'user/edit_review.html', {'form': form, 'review': review})

# Delete review
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('all_reviews')
    return render(request, 'user/delete_review.html', {'review': review})

