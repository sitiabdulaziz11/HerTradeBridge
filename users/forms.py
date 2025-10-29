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
