# Generated by Django 3.2.16 on 2023-01-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_remove_review_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='description',
            field=models.CharField(default='Add description here', max_length=1000),
        ),
    ]
