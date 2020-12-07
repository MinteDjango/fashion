from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.log_out, name="logout"),
    path('login/', views.log_in, name="login")
    ]