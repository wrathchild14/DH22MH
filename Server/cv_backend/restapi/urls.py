from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
]