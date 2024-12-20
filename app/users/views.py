from django.urls  import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from app.users.models import GroupUsers, InviteForGroup
from app.users.forms import UpdateFormsGroupUsers, InviteForGroupForms


class SettingPageViews(ListView):
    '''
    Главная страница настройек
    '''
    model = GroupUsers
    template_name = 'profile.html'


class ListGroupViews(ListView):
    ''' 
    Представление показывающее группы в которые добавлен пользователь 
    '''
    model = GroupUsers

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(group_user=self.request.user)
        return queryset


class UpdateDelGroup(UpdateView):
    '''
    Представление, чтобы удалить группу
    '''
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
    '''
    Представление для обновления группы
    '''
    model = GroupUsers
    form_class = UpdateFormsGroupUsers
    success_url = reverse_lazy('listgroup')


class ListUserProfile(ListView):
    '''
    Представление  для просмотра  запросов пользователя, и для просмтра и настроек аккаунта 
    '''
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


class ListInviteViews(ListView):
    '''
    Представление для просотра приглашений в группу
    '''
    model = InviteForGroup

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(request_user=self.request.user)


class DelAndAcceptInviteView(DeleteView):
    '''
    Представление для принятия приглашения 
    '''
    model = InviteForGroup
    success_url = reverse_lazy('invite')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        group = self.object.group
        group.group_user.add(self.request.user)

        group.save()
        self.object.delete()

        return HttpResponseRedirect(self.success_url)


class DelAndRejectInviteView(DeleteView):
    '''
    Представление для  откланения приглашения
    '''
    model = InviteForGroup
    success_url = reverse_lazy('invite')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


class CreateInvite(CreateView):
    '''
    Создаем инвайт для юзера 
    '''
    model = InviteForGroup
    form_class = InviteForGroupForms
    success_url = reverse_lazy('listgroup')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        print(User.objects.get(username=form.cleaned_data['username']))
        object_ = InviteForGroup.objects.create(
            group=GroupUsers.objects.get(pk=self.kwargs['pk']),
            request_user=User.objects.get(username=form.cleaned_data['username'])
        )
        return HttpResponseRedirect(self.success_url)