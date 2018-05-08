# Generated by Django 2.0.5 on 2018-05-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('icon_class', models.CharField(max_length=100)),
                ('social_media_type', models.CharField(max_length=100)),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
    ]
