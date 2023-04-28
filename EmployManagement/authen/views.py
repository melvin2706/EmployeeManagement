from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
# Create your views here.

def signIn(request):
    return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect('login')