# Generated by Django 2.1.15 on 2020-04-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20200410_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='Articles_Categories_Images')),
            ],
            options={
                'verbose_name': 'Articles Categories',
                'verbose_name_plural': 'Articles Category',
            },
        ),
    ]
