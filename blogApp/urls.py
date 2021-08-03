from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('postComment', views.postComment, name='postComment'),
    path('addPost', views.addPost, name='addPost'),
    path('blogPost/<str:slug>', views.blogPost, name='blogPost'),
    
]
