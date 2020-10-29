from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


def index(request):
    profile = Profile.objects.get(prof_user__username=request.user.username)
   
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Project.objects.all()
        print(posts)
    except Project.DoesNotExist:
        posts = None
    return render(request, 'main/index.html', {'posts': posts, 'form': form, 'profile':profile})
