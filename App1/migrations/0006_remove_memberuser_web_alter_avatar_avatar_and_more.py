# Generated by Django 4.0.5 on 2022-08-10 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0005_remove_avatar_imagen_avatar_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberuser',
            name='web',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='memberuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
