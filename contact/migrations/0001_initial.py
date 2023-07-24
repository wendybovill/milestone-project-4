# Generated by Django 3.2.20 on 2023-07-24 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=75)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_subject', models.CharField(max_length=100)),
                ('contact_message', models.TextField(max_length=1500)),
                ('contact_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('responded', models.BooleanField(default=False)),
            ],
        ),
    ]