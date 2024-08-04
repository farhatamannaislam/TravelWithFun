from django.urls import path
from . import views
from .views import PostList, post_detail, post_create 

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), 
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
]
