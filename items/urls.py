from django.urls import path
from .views import items,add_items

urlpatterns = [
    path('',items),
    path('add/',add_items),
]