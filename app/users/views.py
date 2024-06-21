from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserInfoForm
from .models import UserProfile
from django.contrib import messages

# Create your views here.
def register_view(request):
    # If the request method is POST, it means the form has been submitted
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('posts:list')
    # If the request method is GET, it means the form has not been submitted
    else:
        form = UserCreationForm()
    
    
    return render(request, 'users/register.html', {'form': form})

# login view
def login_view(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            # Login logic
            login(request, form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


# logout view
def logout_view(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('/')


def update_profile_view(request):
    if request.user.is_authenticated:
        try:
            current_user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            messages.error(request, "UserProfile does not exist.")
            return redirect('users:login')

        if request.method == 'POST':
            # Include request.FILES for file uploads
            form = UserInfoForm(request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('/')
        else:
            # Initialize the form with the instance but without POST data for GET requests
            form = UserInfoForm(instance=current_user)

        return render(request, 'users/update_profile.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to update your profile')
        return redirect('users:login')