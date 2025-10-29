
from django.db import models
from product.models import Product, Order 

# Create your models here.


class UserProfile(models.Model): 
    """Model representing a user profile. 
    """
    ROLE_CHOICES = [ ('buyer', 'Buyer'), ('seller', 'Seller'), ]
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"


class Address(models.Model):
    """Model representing an address associated with a user.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='address')
    country = models.CharField(max_length=100, default="Ethiopia")
    city = models.CharField(max_length=100)
    village = models.CharField(max_length=100) 
    village_description = models.TextField(blank=True, null=True) 
    location_type = models.CharField(  max_length=10, choices=[('buyer', 'Buyer'), ('seller', 'Seller')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.country} {self.street}, {self.city}, {self.village}, {self.city}"
        

class Review(models.Model): 
    """ Model handling user reviews.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField() comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user.first_name} {self.user.last_name} - for {self.product.name} - Rating: {self.rating}" 


 class PurchaseHistory(models.Model):
    """ Model to handle user history for seller trust and buyer discount.
    """
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='purchase_history') 
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    purchase_count = models.PositiveIntegerField(default=1) 
    discount_received = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) 
    last_purchase_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.buyer} - {self.product} ({self.purchase_count} times)" 
    
