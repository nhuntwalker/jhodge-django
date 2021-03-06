# Generated by Django 2.0.5 on 2018-05-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('release_date', models.DateField()),
                ('genre', models.TextField()),
                ('credits', models.CharField(max_length=1024)),
                ('trailer', models.URLField()),
                ('description', models.TextField()),
                ('production', models.CharField(max_length=1024)),
                ('excerpt', models.TextField(max_length=85)),
                ('slug', models.SlugField()),
                ('slider_text', models.TextField()),
                ('film_type', models.CharField(max_length=100)),
                ('screenshot', models.ImageField(upload_to='screenshots')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
