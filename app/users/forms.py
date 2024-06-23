from django import forms
from .models import UserProfile

class UserInfoForm(forms.ModelForm):
    
    profile_image = forms.ImageField(
        required=False, 
        label='', 
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
        )
    
    bio = forms.CharField(max_length=500)
    address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    
    class Meta:
        model = UserProfile
        fields = ( 'profile_image', 'bio', 'address', 'phone')