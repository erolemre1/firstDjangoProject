# Generated by Django 3.2.9 on 2023-01-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='file',
            field=models.FileField(db_index=True, null=True, unique=True, upload_to='files'),
        ),
    ]
