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

def signup(request):
    global register_form
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
        register_form = {
            'form': form,
        }
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
def profile(request, username):
    profile = Profile.objects.get(prof_user__username=request.user.username)
    print("profile", profile)
   
    profile_data = {
        'profile': profile
    }
    return render(request, 'profile/profile.html', profile_data)
