# Generated by Django 4.2.1 on 2024-01-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_coursemodels_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodels',
            name='author',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='coursemodels',
            name='link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='coursemodels',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
