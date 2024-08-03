from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
     path('signup/', views.signup, name='signup'),
]

for url in urlpatterns:
    print(url)  # Print each URL pattern for debugging