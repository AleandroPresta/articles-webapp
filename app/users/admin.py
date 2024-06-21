from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile)

# Mix the User model with the UserProfile model
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    
# Extend the User model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = [ "username", "email", "first_name", "last_name", "password"]
    inlines = [UserProfileInLine]
    
# Re-register UserAdmin
admin.site.unregister(User)

admin.site.register(User, UserAdmin)