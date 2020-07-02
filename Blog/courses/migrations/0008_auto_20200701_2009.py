# Generated by Django 3.0.7 on 2020-07-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200701_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='courses',
            name='author',
            field=models.CharField(default='', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='search',
            field=models.CharField(default='', editable=False, max_length=472),
        ),
        migrations.AlterField(
            model_name='courses',
            name='slug',
            field=models.SlugField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='modules',
            name='search',
            field=models.CharField(default='', editable=False, max_length=300),
        ),
        migrations.AlterField(
            model_name='modules',
            name='slug',
            field=models.SlugField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='modules',
            name='subtitle',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='modules',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]