from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board/', views.board_list, name='board_list'),
    path('board/<int:pk>', views.post_detail, name='post_detail'),
    path('board/postnew', views.post_new, name='post_new'),
    path('board/<int:pk>/edit', views.post_edit, name='post_edit'),
]