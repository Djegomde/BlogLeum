from django.shortcuts import render
from django.utils import timezone
from .models import *


# def index(request):
# return render(request, 'accueil/index.html')


def index(request):
    authors = Author.objects.filter(id=2)
    return render(request, 'accueil/index.html', {'authors': authors})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def author_list(request):
    authors_l = Author.objects.all()
    return (request, 'author/author_list.html', {'authors_l': authors_l})
