from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.all_posts, name='list'),
    path('new-post/', views.post_new, name='new-post'),
    path('<slug:slug>', views.post_page, name='page'),
    path('search/', views.search_posts, name='search-view'),
    path('filter/', views.filter_posts, name='filter-view'),
    path('<slug:slug>/new-comment/', views.comment_new, name='new-comment')
]
