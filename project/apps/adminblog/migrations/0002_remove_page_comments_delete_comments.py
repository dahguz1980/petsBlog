# Generated by Django 4.2.2 on 2023-06-13 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
