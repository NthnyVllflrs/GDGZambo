# Generated by Django 2.1.4 on 2019-03-04 09:59

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('video_url', models.URLField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='Draft', max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Story'),
        ),
    ]
