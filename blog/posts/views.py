from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def posts(request, index):
    posts = Post.objects.get(id=index)
    return render (request, 'posts.html', {'posts': posts})