# Generated by Django 3.1.5 on 2021-01-20 06:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_post2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post2',
            new_name='New_post',
        ),
    ]
