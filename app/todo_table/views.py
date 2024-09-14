from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from app.todo_table.models import TemaModels, TaskModels
from app.users.models import GroupUsers
# Create your views here.


class TasksHomePageViews(ListView):
     model = TaskModels

     def get_form_kwargs(self):
          kwargs = super().get_form_kwargs()
          kwargs['user'] = self.request.user
          return kwargs

     # def get_queryset(self):
     #      queryset = super().get_queryset()

     #      id_group = self.kwargs.get('id_group')
     #      id_team = self.kwargs.get('id_team')
     #      if id_group:
     #           group = GroupUsers.objects.get(pk=id_group)
     #           if id_team:
     #                return queryset.filter(pk=id_team, group=group)
     #           return queryset.filter(group=group)
     #      print(queryset)
     #      return queryset

     def get_context_data(self):
          context = super().get_context_data()
          all_group = GroupUsers.objects.filter(group_user=self.request.user)
          context['all_group'] = all_group
          all_team = TemaModels.objects.filter(group__in=all_group)
          context['all_team'] = all_team
          return context