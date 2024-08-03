from django.urls import path
from .import views


urlpatterns = [
     path('signup/', views.signup, name='signup'),
]

for url in urlpatterns:
    print(url)  # Print each URL pattern for debugging