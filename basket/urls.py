from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.item_list, name='item_list'),
    path('basket/add', views.add_item, name='add_item'),
    path('basket/error/', views.error, name='error'),
]