# Generated by Django 5.2.1 on 2025-05-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='article_imgs'),
        ),
    ]
