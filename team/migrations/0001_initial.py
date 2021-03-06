# Generated by Django 2.1.4 on 2019-03-04 09:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('expertise', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, max_length=500, null=True)),
                ('website', models.URLField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo')),
                ('description', models.TextField(max_length=300)),
                ('expertise', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, max_length=500, null=True)),
                ('website', models.URLField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
