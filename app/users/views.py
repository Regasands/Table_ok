from django.shortcuts import render
from django.views.generic import ListView
from app.users.models import GroupUsers
# Create your views here.


class SettingPageViews(ListView):
    model = GroupUsers
    template_name = 'profile.html'