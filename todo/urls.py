from django.contrib import admin
from django.urls import path, include
from .views import todo

urlpatterns = [
    path('a/', include('todo')),
]
