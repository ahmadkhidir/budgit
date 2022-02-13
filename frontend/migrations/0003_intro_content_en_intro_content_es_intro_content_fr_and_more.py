# Generated by Django 4.0.2 on 2022-02-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_people_image_alter_whatwedo_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='content_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='content_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='title_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='title_fr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]