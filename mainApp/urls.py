from django.urls import path, include
from django.conf import settings
import mainApp

urlpatterns = [
path('', mianApp.views.index, name="index"), #리다이렉트용
path('list', mianApp.views.list, name="list"), #리다이렉트용
path('postnew', mianApp.views.postnew, name="postnew") , #리다이렉트용
path('postcreate', mianApp.views.postcreate, name="postcreate"),
path('detail/<int:post_id>', mianApp.views.detail, name="detail"),
path('postedit/<int:post_id>', mianApp.views.postedit, name="postedit"), #리다이렉트용
path('postupdate/<int:post_id>', mianApp.views.postupdate, name="postupdate"),
path('postdelete/<int:post_id>', mianApp.views.postdelete, name="postdelete"),
path('commentcreate/<int:post_id>', mianApp.views.commentcreate, name="commentcreate"),
path('commentdelete/<int:post_id>', mianApp.views.commentdelete, name="commentdelete"),
path('signup', mianApp.views.signup, name = "signup"),
path('signin', mianApp.views.signin, name="signin"),
path('praiseme', mianApp.views.praiseme, name="priaseme")
    ]