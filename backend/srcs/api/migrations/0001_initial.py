# Generated by Django 5.1.2 on 2024-11-27 15:26

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, default='avatars/profile.png', upload_to='avatars/')),
                ('elo', models.IntegerField(default=0)),
                ('language', models.CharField(default='EN')),
                ('last_connection', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships_initiated', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user1', 'user2')},
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(default='pong_1v1', max_length=50)),
                ('user1_score', models.IntegerField(default=0)),
                ('user2_score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_first_opponents', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_second_opponents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Match 1v1',
                'verbose_name_plural': 'Matchs 1v1',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Matchs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(default='pong_2v2', max_length=50)),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matchs_first_opponents_1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matchs_second_opponents_1', to=settings.AUTH_USER_MODEL)),
                ('user3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matchs_first_opponents_2', to=settings.AUTH_USER_MODEL)),
                ('user4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matchs_second_opponents_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Match 2v2',
                'verbose_name_plural': 'Matchs 2v2',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('friend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_chat_id', to='api.friend')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1_position', models.IntegerField(default=4)),
                ('user2_position', models.IntegerField(default=4)),
                ('user3_position', models.IntegerField(default=4)),
                ('user4_position', models.IntegerField(default=4)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_first_opponents_1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_second_opponents_1', to=settings.AUTH_USER_MODEL)),
                ('user3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_first_opponents_2', to=settings.AUTH_USER_MODEL)),
                ('user4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_second_opponents_2', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournaments_winner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tournament 1v1v1v1',
                'verbose_name_plural': 'Tournaments 1v1v1v1',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Blocked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks_initiated', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user1', 'user2')},
            },
        ),
    ]
