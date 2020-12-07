from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.index),
    path('trendings/', views.index),
    path('cart/', views.index),
    path('wishlist/', views.index),
    path('home/', views.index)
    ]