from django.db import models
from django.contrib.auth.models import User


class GroupUsers(models.Model):
    '''
    Модель  группы пользователей, для  объединения  тем под одну группу 
    '''
    group_user = models.ManyToManyField(User, verbose_name='Участники группы', related_name='user_group')
    name = models.CharField(verbose_name='Название группы', max_length=100)
    description = models.CharField(verbose_name='Описание группы', max_length=250)
    admin_user = models.ForeignKey(User, verbose_name='Админ групп', related_name='admin_group', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Группа Пользователей'
        verbose_name_plural = 'Группы Пользователей'


class InviteForGroup(models.Model):
    '''
    Приглашение для пользователя 
    '''
    group = models.ForeignKey(GroupUsers, verbose_name='Группа в которую приглашают', related_name='group', on_delete=models.CASCADE)
    request_user = models.ForeignKey(User, verbose_name='Пользователь, которому отправили запрос', related_name='user', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.group.name}'

    class Meta:
        verbose_name = 'Приглашение в группу'
        verbose_name_plural = 'Приглашения в группу'