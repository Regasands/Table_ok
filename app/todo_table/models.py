from django.db import models
from app.users.models import GroupUsers


class TeskModels(models.Model):
    '''
    Модель задания, плана 
    '''
    class ChoiseColor:
        RED = 'red'
        BLUE = 'blue'
        GREEN = 'green'
        BLACK = 'black'
        WHITE = 'white'
        CHOISE = {
            RED: 'красный',
            BLUE: 'синий',
            GREEN: 'зеленый',
            WHITE: 'белый',
            BLACK: 'черный',
        }
    task =  models.CharField(max_length=100, verbose_name='Имя задания')
    color_border = models.CharField(verbose_name='Цвет_обводки', choices=ChoiseColor.CHOISE)
    color_text = models.CharField(verbose_name='Цвет_текста', choices=ChoiseColor.CHOISE)
    color_background = models.CharField(verbose_name='Цвет_заднегофона', choices=ChoiseColor.CHOISE)
    data = models.DateField(auto_now_add=True, verbose_name='Дата создания задания')
    text_info = models.TextField(max_length=1000, verbose_name='Информация о задание')
    def __str__(self):
        return f'{self.task}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания '


class TemaModels(models.Model):
    '''
    Тема для задания , объеденяет несколько заданий
    '''
    name = models.CharField(verbose_name='Название темы', max_length=100)
    group = models.ForeignKey(GroupUsers, on_delete=models.CASCADE, verbose_name='Група  которая имеет эту тему')
    task = models.ManyToManyField(TeskModels, verbose_name='Задания относящиеся к этой теме ')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        # Create your models her