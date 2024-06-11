from django.shortcuts import render
from .models import Post

# Create your views here.
def all_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/all_posts.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })