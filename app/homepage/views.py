from django.shortcuts import render
from django.views.generic import ListView, View

from app.homepage.models import HomeNewsModel
class HomePageViews(ListView):
    '''
    Отображение главной страницы 
    '''
    model = HomeNewsModel

    def get_queryset(self):
        return super().get_queryset()[:1]
# Create your views here.
