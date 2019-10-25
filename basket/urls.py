from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket_list, name='basket_list'),
    path('basket/new', views.make_basket, name='make_basket'),
    path('basket/<int:pk>', views.basket_detail, name='basket_detail'),
    path('error/', views.basket_error, name='basket_error'),
]