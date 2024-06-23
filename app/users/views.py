from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserInfoForm
from .models import UserProfile
from django.contrib import messages
from posts.models import Post

'''
    Create a logger for the views
'''
import logging

logging_path = './logs/users_views.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    filename=logging_path,
    )

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
    logging.debug('Update profile view')
    logging.info(f'Request: {request}')
    if request.user.is_authenticated:
        try:
            current_user = UserProfile.objects.get(user=request.user)
            logging.debug(f'Current user: {current_user}')
        except UserProfile.DoesNotExist:
            logging.error('UserProfile does not exist.')
            messages.error(request, "UserProfile does not exist.")
            logging.debug('Redirecting to login')
            return redirect('users:login')

        if request.method == 'POST':
            logging.debug('Initializing form for POST request')
            # Include request.FILES for file uploads
            form = UserInfoForm(request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                logging.debug('Form is valid')
                form.save()
                logging.debug('Profile updated successfully')
                messages.success(request, 'Profile updated successfully')
                logging.debug('Redirecting to /')
                return redirect('/')
        else:
            # Initialize the form with the instance but without POST data for GET requests
            logging.debug('Initializing form for GET request')
            form = UserInfoForm(instance=current_user)

        logging.debug('Rendering update_profile.html')
        return render(request, 'users/update_profile.html', {'form': form})
    else:
        logging.error('User is not authenticated')
        messages.error(request, 'You must be logged in to update your profile')
        logging.debug('Redirecting to login')
        return redirect('users:login')
    
    
def profile_view(request, username):
    logging.info(f'Profile view for {username}')
    logging.debug(f'Request: {request}')
    try:
        userprofile = UserProfile.objects.get(user__username=username)
        posts = Post.objects.filter(author=userprofile.user)
        logging.debug(f'User: {userprofile}')
    except UserProfile.DoesNotExist:
        logging.error('UserProfile does not exist.')
        messages.error(request, "UserProfile does not exist.")
        logging.debug('Redirecting to /')
        return redirect('/')
    
    logging.debug(f'Rendering user {userprofile.user}')
    return render(request, 'users/user_profile.html', {'userprofile': userprofile, 'posts': posts})