# Generated by Django 3.2.8 on 2021-10-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20211029_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='jobs/'),
        ),
    ]
