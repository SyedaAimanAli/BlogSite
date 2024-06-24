from django.contrib import admin
from django.urls import path, include
from . import views
from .views import UserPostListView


urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('postComment/', views.postComment, name="postComment"),
    path('addpost/', views.Addblog, name="AddPost"),
    path('user_posts/', UserPostListView.as_view(), name='user_posts'),
    path('edit/<str:slug>', views.edit, name='editBlog'),
    path('delete/<str:slug>', views.delete, name='deleteBlog'),
]
