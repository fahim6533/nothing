from django.contrib import admin
from django.urls import path,include
from App import views

urlpatterns = [
    path('',views.index, name='home'),
    path('home',views.index, name='home'),
    path('blogs', views.blogs, name='blogs')
]
