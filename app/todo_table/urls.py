from django.contrib import admin
from django.urls import path
from app.todo_table.views import TasksHomePageViews

urlpatterns = [
    path('', TasksHomePageViews.as_view(), name="taskshomepage")
]