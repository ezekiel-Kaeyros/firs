# Generated by Django 4.2.1 on 2023-08-31 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_uploadimage_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttexte',
            name='author_id',
        ),
    ]
