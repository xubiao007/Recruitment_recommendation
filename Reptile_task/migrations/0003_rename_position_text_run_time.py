# Generated by Django 3.2 on 2021-05-07 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reptile_task', '0002_rename_requires_page_text_required_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='position',
            new_name='run_time',
        ),
    ]