# Generated by Django 3.2.9 on 2023-01-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.FileField(db_index=True, null=True, upload_to='filese'),
        ),
    ]
