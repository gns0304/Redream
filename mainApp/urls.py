from django.urls import path, include
from django.conf import settings

from mainApp import views

urlpatterns = [
path('', views.index, name="index"), #리다이렉트용
path('list', views.list, name="list"), #리다이렉트용
path('postnew', views.postnew, name="postnew") , #리다이렉트용
path('postcreate', views.postcreate, name="postcreate"),
path('detail/<int:post_id>', views.detail, name="detail"),
path('postedit/<int:post_id>', views.postedit, name="postedit"), #리다이렉트용
path('postupdate/<int:post_id>', views.postupdate, name="postupdate"),
path('postdelete/<int:post_id>', views.postdelete, name="postdelete"),
path('commentcreate/<int:post_id>', views.commentcreate, name="commentcreate"),
path('commentdelete/<int:post_id>', views.commentdelete, name="commentdelete"),
path('signup', views.signup, name = "signup"),
path('signin', views.signin, name="signin"),
path('praiseme', views.praiseme, name="priaseme")
    ]