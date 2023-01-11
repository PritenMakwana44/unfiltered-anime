# Generated by Django 3.2.16 on 2023-01-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='fav_character',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=2000, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
