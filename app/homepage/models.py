from django.db import models


class HomeNewsModel(models.Model):
    topic = models.CharField(verbose_name='Тема')
    text_info = models.TextField(verbose_name='Описание темы(текст)')
    data = models.DateField(auto_now_add=True, verbose_name='Дата создания темы')

    def __str__(self):
        return f"{self.topic}"

    class Meta:
        verbose_name = 'Тема для главной страницы'
        verbose_name_plural = 'Темы для главной страницы'

