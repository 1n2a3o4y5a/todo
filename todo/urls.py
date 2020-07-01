from django.contrib import admin
from django.urls import path, include
.views import todo

urlpatterns = [
    path('a/', include('todo')),
]
