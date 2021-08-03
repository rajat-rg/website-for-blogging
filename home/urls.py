from django.contrib import admin
from django.urls import path
from home import views
from blogApp import views as blogViews
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contact us'),
    path('blogs', blogViews.blogHome, name='blogs'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
    path('search', views.search, name='search'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('user_blogs', views.user_blogs, name='user_blogs'),
]
