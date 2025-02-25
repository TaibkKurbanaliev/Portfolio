from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistartionForm, UserProfileForm

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/sign-in.html',context)

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistartionForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:sign-in'))
    else:
        form = UserRegistartionForm()
    context = {'form': form}
    return render(request, 'users/sign-up.html',context)

def profile_change(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    form = UserProfileForm(instance=request.user)
    print(request.user.image)
    context = { 'form': form }
    return render(request, 'users/profile_change.html', context)

def profile(request):
    username = request.GET.get('username')
    if username:
        user = get_object_or_404(User, username=username)
    else:
        if request.user.is_authenticated:
            user = request.user
        else:
            return redirect('')
    context = {
        'user_profile': user,
        'is_owner': request.user.is_authenticated and request.user == user,  # Проверка, является ли текущий пользователь владельцем профиля
    }
    
    return render(request, 'users/profile.html', context)