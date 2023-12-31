# Generated by Django 3.2.20 on 2023-07-21 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20230720_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.BooleanField(blank=True, default=False, null=True)),
                ('default_full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('default_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user_email_subject', models.CharField(max_length=100)),
                ('user_email_message', models.TextField(max_length=2000)),
                ('user_contact_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='email_images/')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='full_name', to='profiles.userprofile')),
            ],
        ),
    ]
