# Generated by Django 4.0 on 2022-01-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='kcal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='protein',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sugar',
            field=models.IntegerField(default=0),
        ),
    ]
