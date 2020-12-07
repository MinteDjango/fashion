from django.urls import path
from . import views

urlpatterns = [
    path('api/items/', views.Items.as_view()),
    ]