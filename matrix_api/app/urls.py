from django.urls import path
from . import views

urlpatterns = [
    path('inverse/', views.inverse)
]