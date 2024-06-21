from django import forms
from .models import UserProfile

class UserInfoForm(forms.ModelForm):
    
    profile_image = forms.ImageField(
        required=False, 
        label='', 
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
        )
    
    class Meta:
        model = UserProfile
        fields = ( 'profile_image',)