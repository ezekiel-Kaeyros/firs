# Generated by Django 4.2.1 on 2023-05-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_postfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
