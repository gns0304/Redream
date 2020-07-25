from django.shortcuts import render, redirect
from .models import Account

# Create your views here.
def signUp(request):
    return render(request, 'signup.html')

def signUp_complete(request) :
    return render(request, 'signupcomplete.html')

def signUp_check(request) :
    return redirect('index.html')