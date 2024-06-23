from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update-profile/', views.update_profile_view, name='update-profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('user-posts/', views.user_posts_view, name='user-posts'),

]