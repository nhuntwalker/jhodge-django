# Generated by Django 2.0.5 on 2018-05-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='order',
            field=models.IntegerField(unique=True, verbose_name='Menu Order'),
        ),
    ]
