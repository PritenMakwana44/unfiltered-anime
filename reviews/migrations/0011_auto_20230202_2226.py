# Generated by Django 3.2.16 on 2023-02-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_comments_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='hidden',
        ),
        migrations.AddField(
            model_name='comments',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
