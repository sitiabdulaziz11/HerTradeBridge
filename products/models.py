from django.db import models

from users.models import UserProfile, Address

# Create your models here.

class Product(models.Model): 
    """Model representing a product. 
    """
    STATUS_CHOICES = [
        ('available', 'Available'), 
        ('finished', 'Finished'), 
        ]
    
    name = models.CharField(max_length=200)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.CharField(max_length=20,  blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    amount = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='products')  # , null=True, blank=True
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    
    image = models.ImageField(upload_to='products/images', blank=True, null=True) 
    video = models.FileField(upload_to='products/videos/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" {self.id} -  {self.name}"
    
class Order(models.Model): 
    """
    Model representing an order for a product.
    """
    STATUS_CHOICES = [ ('pending', 'Pending'), ('deliverd', 'Deliverd'), ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders') 
    order_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50, blank=True)
    order_description = models.TextField(blank=True) 
    ordered_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Order #{self.id} - {self.product.name} by {self.buyer.first_name}"
