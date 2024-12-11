from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Santosh',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 11, 2024'
    },
        {
        'author': 'Saurab',
        'title': 'Blog Post 2',
        'content': 'Sencond post in the blog content',
        'date_posted': 'December 11, 2024'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')