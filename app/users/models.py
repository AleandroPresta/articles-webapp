from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='../static/assets/user-fallback.webp', blank=True)
    bio = models.TextField(max_length=500, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    
    
    def __str__(self):
        return self.user.username

# Create automatically the user profile when a new user is created 
# (the fields will be added by the user in his user's modification page)

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
        
# Connect the signal to the function
post_save.connect(create_profile, sender=User)