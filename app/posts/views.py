from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify

# Create your views here.
def all_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/all_posts.html', {'posts': posts, 'categories': Post.CATEGORY_CHOICES})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user
            newpost.slug = slugify(newpost.title)
            # Check if exist another post with the same slug
            if Post.objects.filter(slug=newpost.slug).exists():
                # If exist, add a number to the end slug
                newpost.slug = newpost.slug + '-' + str(Post.objects.filter(slug=newpost.slug).count())
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })


def search_posts(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        posts = Post.objects.filter(title__contains=search_query)
        return render(request, 'posts/search_posts.html', {'query':search_query, 'posts':posts})
    else:
        return render(request, 'posts:list')