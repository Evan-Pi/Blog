# Generated by Django 3.1.4 on 2021-02-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210226_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article',
            field=models.TextField(),
        ),
    ]
