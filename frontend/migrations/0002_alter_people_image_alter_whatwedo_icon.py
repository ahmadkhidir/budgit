# Generated by Django 4.0.2 on 2022-02-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='icon',
            field=models.ImageField(upload_to='images'),
        ),
    ]