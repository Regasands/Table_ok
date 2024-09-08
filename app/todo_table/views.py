from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from app.todo_table.models import TemaModels, TaskModels
# Create your views here.


class TasksHomePageViews(ListView):
     model = TaskModels
     