from django.urls import path
from django.shortcuts import redirect

from . import views


urlpatterns = [
    path('', lambda _: redirect('index')),
    path('index', views.index, name='index')
]
