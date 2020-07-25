from django.urls import path, include
from django.conf import settings
import mainApp.views

urlpatterns = [
path('', mainApp.views.index, name="index"), #리다이렉트용
path('list', mainApp.views.list, name="list"), #리다이렉트용
path('postnew', mainApp.views.postnew, name="postnew") , #리다이렉트용
path('postcreate', mainApp.views.postcreate, name="postcreate"),
path('detail/<int:post_id>', mainApp.views.detail, name="detail"),
path('postedit/<int:post_id>', mainApp.views.postedit, name="postedit"), #리다이렉트용
path('postupdate/<int:post_id>', mainApp.views.postupdate, name="postupdate"),
path('postdelete/<int:post_id>', mainApp.views.postdelete, name="postdelete"),
path('commentcreate/<int:post_id>', mainApp.views.commentcreate, name="commentcreate"),
path('commentdelete/<int:post_id>', mainApp.views.commentdelete, name="commentdelete"),
path('signup', mainApp.views.signup, name = "signup"),
path('signin', mainApp.views.signin, name="signin"),
path('praiseme', mainApp.views.praiseme, name="priaseme")
    ]