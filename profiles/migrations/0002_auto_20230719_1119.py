# Generated by Django 3.2.20 on 2023-07-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_title',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
