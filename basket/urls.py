from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket_list, name='basket_list'),
    path('basket/add', views.add_basket, name='add_basket'),
    path('basket/add/newitem', views.add_item, name='add_item'),
    path('basket/<int:pk>', views.basket_detail, name="basket_detail")
]