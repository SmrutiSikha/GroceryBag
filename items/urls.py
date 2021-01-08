from django.urls import path
from .views import items,add_items,add_page,delete_items

urlpatterns = [
    path('',items),
    path('addPage/',add_page,name='addPage'),
    path('add/',add_items,name='addItems'),
    path('delete/',delete_items,name='deleteItems')
]