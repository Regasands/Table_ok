# Generated by Django 5.0.6 on 2024-09-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_table', '0002_alter_teskmodels_color_background_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teskmodels',
            old_name='data',
            new_name='date',
        ),
    ]