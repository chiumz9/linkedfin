# Generated by Django 4.0.4 on 2022-05-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]
