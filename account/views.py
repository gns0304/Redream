from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm, SigninForm, UserForm
from .models import RedUser


# Create your views here.
#회원가입 
def signUp(request):
    return render(request, 'signup.html')
    

def signUp_complete(request) :
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid() :
            if user == donator :
                new_user = user.objects.create_user(nickname=form.cleaned_Data['nickname'],
                number=form.cleaned_data['number'], bloodtype=form.cleaned_data['bloodtype'],
                location=form.cleaned_data['location'], donationcount=form.cleaned_data['donationcount'])

            else:
                new_user = user.objects.create_user(nickname=form.cleaned_Data['nickname'],
                number=form.cleaned_data['number'], bloodtype=form.cleaned_data['bloodtype'],
                location=form.cleaned_data['location'], description=form.cleaned_data['description'])        
        login(request, new_user)
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
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return render(request, 'list.html')
    else :
        form = PostForm()
        return render(request, 'postcreate.html', {'form': form})

#글찾기
def find_page(request) :
    return render(request, 'list.html')

def comment_create(request, comment_id) :
    onepost = get_object_or_404(HelpPost, pk=comment_id)
    return render(request, 'list.html')

def comment_delete(request, post_id, comment_id) :
    comment = get_object_or_404(BlogComment, id=comment_id, post_id=post_id)
    comment.delete()
    return redirect(str(post_id))

def post_update(request, pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST" :
        form = PostForm(request.POST, instance=post)
        if form.is_valid() :
            form = form.save(commit=False)
            form.save()
            return render('edit_complete.html')
    else:
        form = PostForm(instance=post)
        return render(requst, 'list.html', {'form': form})

def post_update_check(request)
    return redirect('list.html')

def post_delete(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return render(request, 'delete_complete.html')



