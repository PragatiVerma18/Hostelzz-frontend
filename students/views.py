from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
#from contacts.models import Contact

def register(request):
  return render(request, 'students/register.html')

def login(request):
  return render(request, 'students/login.html')

def logout(request):
  return redirect('about')

def dashboard(request):
  return render(request, 'students/dashboard.html')
