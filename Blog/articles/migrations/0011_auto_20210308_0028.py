# Generated by Django 3.1.7 on 2021-03-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210303_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
    ]
