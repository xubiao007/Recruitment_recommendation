# Generated by Django 3.2 on 2021-05-14 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_information', '0004_alter_user_pwd'),
        ('Job_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Job_information.work')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_information.user')),
            ],
        ),
    ]
