from django.contrib import admin
from django.urls import path
from .views import postStudent

urlpatterns = [
    path('add-student/',postStudent)
]