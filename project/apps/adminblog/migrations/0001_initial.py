# Generated by Django 4.2.2 on 2023-06-12 19:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('commentDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='Titulo Página')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen Principal')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('comments', models.ManyToManyField(blank=True, to='adminblog.comments')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
