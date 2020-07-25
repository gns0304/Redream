from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import PraiseMePost, praiseMeComment
from .form import PostingForm

# Create your views here.

def main(request):
    posts = PraiseMePost.objects.all()
    return render(request, 'main.html', {'posts':posts})

def praisePostCreate(request):
    if request.method == "POST":
        form = PostingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostingForm()
        return render(request, 'create.html', {'form', form})

def praisePostNew(request):
    

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostingForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostingForm(instance=post)
        return render(request, 'create.html', {'form': form})