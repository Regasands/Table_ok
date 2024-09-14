from django.contrib import admin
from app.todo_table.models import TaskModels, TemaModels
admin.site.register(TaskModels)
@admin.register(TemaModels)
class TemaModelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')  # Укажите поля для отображения в списке
    fields = ('name', 'group')  # Укажите поля для отображения в форме редактирования
