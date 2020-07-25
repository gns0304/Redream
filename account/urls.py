
from django.urls import path, include
from django.conf import settings
import account.views

urlpatterns = [
path('signup', account.views.signup, name="signup"),
path('signin', account.views.signin, name="signin"),
    ]

