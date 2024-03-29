from django.shortcuts import render, redirect
from blog.models import Post
from django.http import HttpResponse

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')


def robots_txt(request):
    text = [
        "User-Agent: + ",
        "Disalow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")
