# Generated by Django 4.1.3 on 2022-11-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Title', max_length=255),
        ),
    ]