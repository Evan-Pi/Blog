# Generated by Django 3.1.7 on 2021-02-27 22:45

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210227_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='module',
            field=froala_editor.fields.FroalaField(),
        ),
    ]