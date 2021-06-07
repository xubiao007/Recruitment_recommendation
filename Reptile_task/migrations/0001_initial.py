# Generated by Django 3.2 on 2021-05-07 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_information', '0004_alter_user_pwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_key', models.CharField(max_length=30, verbose_name='职位关键词')),
                ('total_page', models.IntegerField(null=True, verbose_name='爬取页数')),
                ('requires_page', models.IntegerField(null=True, verbose_name='爬取页数')),
                ('state', models.CharField(default='无', max_length=16, null=True, verbose_name='状态')),
                ('position', models.CharField(max_length=20, null=True, verbose_name='运行时间')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_information.user')),
            ],
        ),
    ]