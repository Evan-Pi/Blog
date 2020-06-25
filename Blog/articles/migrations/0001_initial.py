# Generated by Django 3.0.7 on 2020-06-25 16:25

import ckeditor_uploader.fields
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
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('search', models.CharField(default='', editable=False, max_length=512)),
                ('slug', models.SlugField(editable=False, max_length=256)),
                ('subtitle', models.TextField(blank=True, max_length=256)),
                ('image', models.ImageField(default='', upload_to='Articles_Images')),
                ('article', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField()),
                ('author', models.CharField(default='', editable=False, max_length=256)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='ArticlesCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='Articles_Categories_Images')),
            ],
            options={
                'verbose_name': 'Articles Category',
                'verbose_name_plural': 'Articles Categories',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('author_image', models.ImageField(blank=True, default='', upload_to='Comments_Author_Images')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='SubComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('author_image', models.ImageField(blank=True, default='', upload_to='Comments_Author_Images')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Comments')),
            ],
            options={
                'verbose_name': 'Subcomment',
                'verbose_name_plural': 'Subcomments',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.ArticlesCategories'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
