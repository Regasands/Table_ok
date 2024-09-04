from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GroupUsers(models.Model):
    group_user = models.ManyToManyField(User, verbose_name='Участники группы', related_name='user_group')
    name = models.CharField(verbose_name='Название группы', max_length=100)
    description = models.CharField(verbose_name='Описание группы', max_length=250)
    admin_user = models.ForeignKey(User, verbose_name='Админ групп', related_name='admin_group', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Группа Пользователей'
        verbose_name_plural = 'Группы Пользователей'