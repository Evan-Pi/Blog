# Generated by Django 3.0.7 on 2020-06-30 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200629_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='module',
        ),
        migrations.AddField(
            model_name='modules',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Courses'),
        ),
    ]
