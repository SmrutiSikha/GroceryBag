from django.urls import path, include
from .views import user_register

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/',user_register, name="user_register_page"),
]