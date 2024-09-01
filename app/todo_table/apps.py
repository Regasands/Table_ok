from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_table'

class CoreConfig(AppConfig):
    name = 'app.todo_table'
    