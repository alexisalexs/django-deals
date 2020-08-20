from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import HomePage
urlpatterns = [
    path('', HomePage.as_view(), name='homepage')

]