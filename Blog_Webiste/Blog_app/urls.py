from django.contrib import admin
from django.urls import path,include
from Blog_app import views

urlpatterns = [
    path('',views.index, name='home'),
    path('home',views.index, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('category_blogs/<str:slug>/', views.category_blogs, name='category_blogs'),
    path('tag_blogs/<str:slug>/', views.tag_blogs, name='tag_blogs'),
    path('blog/<str:slug>/', views.blog_details, name='blog_details'),
    path('add_reply/<int:blog_id>/<int:comment_id>/', views.add_reply, name='add_reply'),
    path('like_blog/<int:blog_id>/', views.like_blog, name='like_blog'),
    path('search_blog/', views.search_blog, name='search_blog'),
    path('my_blogs/', views.my_blogs, name='my_blogs'),
    path('add_blog/', views.add_blog, name='add_blog'),
    
]