# Generated by Django 3.0.8 on 2020-07-22 16:19

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('search', models.CharField(default='', editable=False, max_length=472)),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('image', models.ImageField(default='', upload_to='Courses_Images')),
                ('use_image_as_background_in_course', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField()),
                ('author', models.CharField(default='', editable=False, max_length=64)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='CoursesCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='Courses_Categories_Images')),
            ],
            options={
                'verbose_name': 'Course Category',
                'verbose_name_plural': 'Courses Categories',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('search', models.CharField(default='', editable=False, max_length=300)),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('subtitle', models.CharField(blank=True, max_length=150)),
                ('module', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField()),
                ('order', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.CoursesCategories'),
        ),
        migrations.AddField(
            model_name='courses',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
