# Generated by Django 3.0.7 on 2020-07-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_modules_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
