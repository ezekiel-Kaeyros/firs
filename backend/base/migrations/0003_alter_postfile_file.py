# Generated by Django 4.2.1 on 2023-05-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_postfile_posttexte_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_folder'),
        ),
    ]
