from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

# Create your views here.
def loginv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {'error':"user doesn't exist", 'form':LoginForm()}
            return render(request, 'audit/login.html', context)
    else:
        context = {'error':"", 'form':LoginForm()}
        return render(request, 'audit/login.html', context)

@login_required
def logoutv(request):
    logout(request)
    return render(request, 'audit/logout.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username,email,password1)
            user.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {'error':"password doesn't match", "form":RegisterForm()}
            return render(request, 'audit/register.html', context)
    else:
        context = {'error':"", "form":RegisterForm()}
        return render(request, 'audit/register.html', context)