# Generated by Django 3.1.4 on 2021-02-27 15:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210226_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article',
            field=tinymce.models.HTMLField(),
        ),
    ]