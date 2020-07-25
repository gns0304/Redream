from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
path('', views.index, name="index"), #리다이렉트용 : done
path('list', views.postList, name="list"), #리다이렉트용 : done
path('postnew', views.postnew, name="postnew") , #리다이렉트용 : done
path('postcreate', views.postcreate, name="postcreate"), # done
path('detail/<int:post_id>', views.detail, name="detail"), # done
path('postedit/<int:post_id>', views.postedit, name="postedit"), #리다이렉트용
path('postupdate/<int:post_id>', views.postupdate, name="postupdate"),
path('postdelete/<int:post_id>', views.postdelete, name="postdelete"),
path('commentcreate/<int:post_id>', views.commentcreate, name="commentcreate"),
path('commentdelete/<int:post_id>', views.commentdelete, name="commentdelete"),
path('praiseme', views.praiseme, name="priaseme")
    ]