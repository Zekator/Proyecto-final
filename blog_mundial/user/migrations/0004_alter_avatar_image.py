# Generated by Django 4.0.5 on 2022-06-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatars'),
        ),
    ]
