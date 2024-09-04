from django.contrib import admin
from app.users.models import GroupUsers


@admin.register(GroupUsers)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'admin_user')  # Поля, которые будут отображаться в списке
    filter_horizontal = ('group_user',)  # Добавляет горизонтальный виджет для поля ManyToMany
    # или используйте:
    # filter_vertical = ('group_user',)  # Для вертикального вида

    # Вы также можете настроить, какие поля будут отображаться на странице редактирования
    fields = ('name', 'description', 'admin_user', 'group_user')
# Register your models here.
