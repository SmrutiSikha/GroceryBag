from django.urls import path
from .views import items,add_items,add_page,delete_items,update_items_page,updated_items,filter_items

urlpatterns = [
    path('',items, name='allItems'),
    path('addPage/',add_page,name='addPage'),
    path('add/',add_items,name='addItems'),
    path('delete/',delete_items,name='deleteItems'),
    path('updates/<int:pk>', update_items_page, name='updatepage'),
    path('updated/',updated_items,name='updateItems'),
    path('filter/',filter_items,name='filterItems'),
]