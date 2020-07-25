from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import PraiseMePost, DonatorPraiseMeComment, ReceiverPraiseMeComment
from .form import PostingForm


# Create your views here.

def main(request):
    post = Post.object.all()
    return render(request, 'praiseMeApp/main.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        form = PostingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostingForm()
        return render(request, 'praiseMeApp/create.html', {'form', form})

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
        return render(request, 'praiseMeApp/create.html', {'form': form})