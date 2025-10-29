from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """ Forms that handle user profile.
    """
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'country', 'city', 'village', 'village_description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'product', 'rating', 'comment']
