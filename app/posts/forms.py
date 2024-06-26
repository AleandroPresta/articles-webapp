from django import forms
from .models import Post, Comment

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'banner']

class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'banner']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
