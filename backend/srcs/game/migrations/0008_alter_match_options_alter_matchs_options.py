# Generated by Django 5.1.2 on 2024-11-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_rename_mode_match_game_rename_mode_matchs_game'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['-created_at'], 'verbose_name': 'Match 1v1', 'verbose_name_plural': 'Matchs 1v1'},
        ),
        migrations.AlterModelOptions(
            name='matchs',
            options={'ordering': ['-created_at'], 'verbose_name': 'Match 2v2', 'verbose_name_plural': 'Matchs 2v2'},
        ),
    ]