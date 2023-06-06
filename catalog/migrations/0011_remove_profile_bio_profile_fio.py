# Generated by Django 4.2 on 2023-06-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_profileadmin_alter_profile_options_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='fio',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]