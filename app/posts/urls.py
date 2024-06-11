from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<slug:slug>', views.post_page, name='page'),
]