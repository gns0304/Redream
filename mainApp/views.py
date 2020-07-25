from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import get_user_model

from account.models import Donator, Receiver
from .models import HelpPost, DonatorComment, ReceiverComment
from .form import PostingForm, DonatorCommentForm, ReceiverCommentForm

def index(request):
    return render(request, 'index.html')

def postList(request):
    posts = HelpPost.objects.all()
    return render(request, 'list.html')

def detail(request, post_id):
    post = get_object_or_404(HelpPost, pk=post_id)
    
    donatorComments = DonatorComment.objects.filter(post_id=post_id).order_by('-pub_data')
    receiverComments = receiverComment.objects.filter(post_id=post_id).order_by('-pub_data')

    tot

    commentForm = commentFormReturn(request)

    return render(request, 'detail.html', {'post':post, 'commentForm':commentForm})

def postnew(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            content = form.save()
            content.pub_date = timezone.now()
            content.save()
            return redirect('list')
    else:
        form = PostingForm()
        return render(request, 'postcreate.html', {'form':form})

def postcreate(request):
    new_post = HelpPost()
    new_post.deadLine = request.POST['deadLine']
    new_post.body = request.POST['body']
    new_post.pub_date = timezone.datetime.now()
    new_post.save()

    return redirect('/detail/' + str(new_post.id))

def postedit(request, post_id):
    post = get_object_or_404(HelpPost, pk=post_id)
    return render(request, 'postedit.html', {'post':post})

def postupdate(request, post_id):
    modified_post = HelpPost()
    modified_post.deadLine = request.POST['deadLine']
    modified_post.body = request.POST['body']
    modified_post.pub_date = timezone.datetime.now()
    modified_post.save()

    return redirect('/detail/' + str(modified_post.id))

def postdelete(request, post_id):
    target_post = get_object_or_404(HelpPost, pk=post_id)
    target_post.delete()
    return redirect('list')

def commenting(request, post_id):
    


def commentFormReturn(request):
    userInfo = request.user.get_user_model()

    if(type(userInfo) == Donator):
        commentForm = DonatorCommentForm()

    elif(type(userInfo) == Receiver):
        commentForm = ReceiverCommentForm()
    
    else:
        commentForm = None
    
    return commentForm
