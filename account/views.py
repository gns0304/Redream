from django.shortcuts import render, redirect
from .forms import PostForm, SigninForm, UserForm

# Create your views here.
#회원가입 
def signUp(request):
    return render(request, 'signup.html')
    

def signUp_complete(request) :
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid() :
            if user = donator
            new_user = user.objects.create_user(nickname=form.cleaned_Data['nickname'],
            number=form.cleaned_data['number'], bloodtype=form.cleaned_data['bloodtype'],
            location=form.cleaned_data['location'])
    form = PostForm(request.POST)
    form.save()
    return render(request, 'signupcomplete.html')

def signUp_check(request) :
    return redirect('index.html')

#로그인
def signIn(request) :
    return render(request, 'signin.html')

def signIn_check(request) :
    return redirect('index.html')

#글쓰기
def write(request) :
    return render('postcreate.html')

def write_page(request) :

    return render(request, 'list.html')

