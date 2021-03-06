# Generated by Django 3.2 on 2021-05-01 12:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User_information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=60, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='exp',
            field=models.CharField(max_length=20, null=True, verbose_name='经验'),
        ),
        migrations.AlterField(
            model_name='user',
            name='skill',
            field=models.CharField(max_length=20, null=True, verbose_name='技能'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(max_length=20, null=True, verbose_name='职称'),
        ),
        migrations.CreateModel(
            name='Await',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('quan', '全职'), ('jian', '兼职'), ('shix', '实习'), ('bux', '不限')], default='不限', max_length=10, verbose_name='职业类型')),
                ('city', models.CharField(default='全国', max_length=10, verbose_name='期待城市')),
                ('major', models.CharField(max_length=16, null=True, verbose_name='专业方向')),
                ('position', models.CharField(max_length=20, null=True, verbose_name='职位名称')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('user_await', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_information.user')),
            ],
        ),
    ]
