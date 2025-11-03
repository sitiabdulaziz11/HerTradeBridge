from django import forms

from .models import UserProfile, Address, Review


class UserProfileForm(forms.ModelForm):
    """ Forms that handle user profile.
    """
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'country', 'city', 'village', 'location_type', 'village_description', ] #'created_at', 'updated_at'
                 # ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'product', 'rating', 'comment']
