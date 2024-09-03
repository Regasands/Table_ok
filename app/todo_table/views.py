from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from app.todo_table.models import TemaModels
# Create your views here.


class TesksHomePageViews(ListView):
     model = TemaModels
     