from django.contrib import admin
from django.urls import path
from app.todo_table.views import TesksHomePageViews

urlpatterns = [
    path('', TesksHomePageViews.as_view(), name="teskshomepage")
]