from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sign_up/', views.sign_up, name='signup'),
]