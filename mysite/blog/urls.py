from django.urls import path

from blog import admin
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]