# Generated by Django 4.2.2 on 2023-06-11 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='createdDate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='facebookLink',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='instagramLink',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedinLink',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitterLink',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updateDate',
        ),
    ]