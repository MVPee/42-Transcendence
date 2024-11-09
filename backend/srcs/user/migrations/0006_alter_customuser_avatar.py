# Generated by Django 5.1.2 on 2024-11-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='/frontend/media/avatars/profile.png', upload_to='avatars/'),
        ),
    ]
