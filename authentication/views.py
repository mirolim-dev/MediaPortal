from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import RegisterForm
# Create your views here.

def login_view(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User or password wrong')
    context= {}
    return render(request, 'authentication/login.html', context)


def register_view(request):#done
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.warning(request, f"{form.errors}")
        
    context = {
        'form': form,
    }
    return render(request, 'authentication/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')