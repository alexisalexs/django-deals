from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import test
from .rest_views import ItemListCreate
urlpatterns = [
    path('what', test.as_view(), name='homepage'),
    path('api/item/',ItemListCreate.as_view(),name='restful_item' )

]