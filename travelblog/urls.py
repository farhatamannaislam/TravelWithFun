from django.urls import path
from . import views
from .views import PostList, post_detail, post_create,post_edit, post_delete

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), 
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', post_delete, name='post_delete'),
    path('post/new/', post_create, name='post_create'),
]
