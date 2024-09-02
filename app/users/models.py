from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GroupUsers(models.Model):
    group_user = models.ManyToManyField(User, verbose_name='Участники группы')
    name = models.CharField(verbose_name='Название группы', max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Группа Пользователей'
        verbose_name_plural = 'Группы Пользователей'