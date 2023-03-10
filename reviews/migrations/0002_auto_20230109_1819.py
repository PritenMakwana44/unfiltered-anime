# Generated by Django 3.2.16 on 2023-01-09 18:19

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('type', models.CharField(choices=[('FILM', 'Film'), ('SHOW', 'Show')], default='Film', max_length=4)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('release_year', models.PositiveSmallIntegerField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=300)),
                ('review', models.CharField(max_length=300, unique=True)),
                ('fav_character', models.CharField(max_length=200)),
                ('downvotes', models.ManyToManyField(blank=True, related_name='review_downvote', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='review_upvote', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review_page', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.AlterField(
            model_name='comments',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review'),
        ),
        migrations.AlterField(
            model_name='watchlater',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlater', to='reviews.review'),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
