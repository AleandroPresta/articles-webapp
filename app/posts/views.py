from django.shortcuts import render, redirect
from .models import Post, Comment
from .models import CATEGORY_CHOICES
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify

import logging

logging_path = 'logs/posts_viwes.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename=logging_path,
    )

# Create your views here.
def all_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/all_posts.html', {'posts': posts, 'categories': CATEGORY_CHOICES})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    logging.debug(f"Post: {post}")
    logging.debug(f"Comments: {comments}")
    return render(request, 'posts/post_page.html', { 'post': post, 'comments': comments })

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
        return render(request, 'posts/search_posts.html', {'query':search_query, 'posts':posts, 'categories': CATEGORY_CHOICES})
    else:
        return render(request, 'posts:list')

    
def filter_posts(request):
    if request.method == "POST":
        filter_query = request.POST.get('select_query')
        filter_query_name_to_show = Post.convert_code_to_name(filter_query)
        if filter_query == 'all':
            posts = Post.objects.all()
            filter_query_name_to_show = 'All'
        else:
            posts = Post.objects.filter(category=filter_query)
        print(f"Posts: {posts}")
        return render(request, 'posts/filter_posts.html', {'query': filter_query_name_to_show, 'posts': posts, 'categories': CATEGORY_CHOICES})
    else:
        posts = Post.objects.all()
        return render(request, 'posts/filter_posts.html', {'posts': posts})
    

@login_required(login_url="/users/login/")
def comment_new(request, slug):
    logging.info(f"Comment view on post with slug: {slug}")
    
    if request.method == 'POST':
        logging.debug(f"Comment new POST request")
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            logging.debug(f'Comment form is valid')
            newcomment = form.save(commit=False)
            newcomment.author = request.user
            
            post = Post.objects.get(slug=slug)
            newcomment.post = post
            
            newcomment.save()
            logging.debug(f'Comment saved: {newcomment} saved for post {post}')
            logging.info(f'Comment saved successfully, redirecting to post {slug}')
            return redirect('posts:page', slug=slug)
        
    else:
        form = forms.CreateComment()
        logging.debug(f"Comment new GET request")
    
    return render(request, 'posts/comment_new.html', {'form': form, 'slug': slug})
