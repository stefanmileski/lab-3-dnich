from django.shortcuts import render
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'index.html', {})


def posts(request):
    queryset = Post.objects.all()
    context = {"posts": queryset, "form": PostForm}
    return render(request, 'post.html', context=context)
