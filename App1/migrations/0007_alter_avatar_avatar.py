# Generated by Django 4.0.5 on 2022-08-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_alter_avatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/avatarDefault.png', null=True, upload_to='avatar'),
        ),
    ]
