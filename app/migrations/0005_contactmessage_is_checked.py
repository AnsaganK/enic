# Generated by Django 5.2.1 on 2025-05-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contactmessage_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='is_checked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
