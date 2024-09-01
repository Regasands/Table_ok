from django.contrib import admin
from django.urls import path
from app.todo_table.views import wee

urlpatterns = [
    path('', wee, name='se')
]