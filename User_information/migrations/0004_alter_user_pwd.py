# Generated by Django 3.2 on 2021-05-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_information', '0003_alter_await_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
    ]
