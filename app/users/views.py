from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.urls  import reverse_lazy
from app.users.models import GroupUsers
from app.users.forms import UpdateFormsGroupUsers
# Create your views here.


class SettingPageViews(ListView):
    model = GroupUsers
    template_name = 'profile.html'

class ListGroupViews(ListView):
    model = GroupUsers

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(group_user=self.request.user)
        return queryset


class UpdateDelGroup(UpdateView):
    model = GroupUsers
    fields = []
    template_name = 'users/delgroup.html'

    def get_object(self, queryset=None):
        return GroupUsers.objects.get(pk=self.kwargs.get('pk'))

    def form_valid(self , form):
        group = self.get_object()
        group.group_user.remove(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listgroup')


class UpdateAdminGroup(UpdateView):
    model = GroupUsers
    form_class = UpdateFormsGroupUsers
    success_url = reverse_lazy('listgroup')


class ListUserPeofile(ListView):
    model = GroupUsers
    template_name = 'users/profilelist.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(group_user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        if queryset:
            context['len_group'] = len(queryset)
        else:
            context['len_group'] = 0
        return context