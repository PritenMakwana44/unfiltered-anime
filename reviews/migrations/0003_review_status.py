# Generated by Django 3.2.16 on 2023-01-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230109_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
