from django.urls import path, include
from django.conf import settings
from praiseMeApp import views

urlpatterns = [
    path('', praiseMeApp.views.create, name='main'),
    path('layout/', praiseMeApp.views.layout, name='layout'),
    path('board/', praiseMeApp.views.board, name='board'),
    path('create', praiseMeApp.views.create, name='create'),
    path('read/', praiseMeApp.views.read, name='read'),
    path('update/<int:pk>', praiseMeApp.views.update, name='update'),
    path('delete/<int:pk>', praiseMeApp.views.delete, name='delete'),
    path('signin', praiseMeApp.views.signin, name='signin'),
    path('signup', praiseMeApp.views.signup, name='signup'),
    path('commentupdate/<int:pk>', praiseMeApp.views.commentupdate, name='commentupdate'),
    path('commentdelete/<int:pk>', praiseMeApp.views.commentdelete, name='commentdelete')                                         
]