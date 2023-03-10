# Generated by Django 4.1.6 on 2023-02-14 18:24

import api.v1.accounts.services
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


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
                ('number_id', models.CharField(max_length=8, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='Raqam 13 ta belgidan iborat bolishi kerak. P.s: +998912345678', regex='^\\+?998?\\d{9}$')])),
                ('balance', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('about', models.CharField(blank=True, max_length=255)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(default='user/defaultuser/defaultuser.png', upload_to=api.v1.accounts.services.upload_avatar_path)),
                ('other_skills', models.CharField(blank=True, max_length=300)),
                ('hobby', models.CharField(blank=True, max_length=300)),
                ('resume', models.FileField(blank=True, null=True, upload_to=api.v1.accounts.services.upload_resume_path)),
                ('edu1_name', models.CharField(blank=True, max_length=250)),
                ('edu1_direction', models.CharField(blank=True, max_length=150)),
                ('edu1_start_date', models.DateField(blank=True, null=True)),
                ('edu1_end_date', models.DateField(blank=True, null=True)),
                ('edu1_now', models.BooleanField(default=False)),
                ('edu2_name', models.CharField(blank=True, max_length=250)),
                ('edu2_direction', models.CharField(blank=True, max_length=150)),
                ('edu2_start_date', models.DateField(blank=True, null=True)),
                ('edu2_end_date', models.DateField(blank=True, null=True)),
                ('edu2_now', models.BooleanField(default=False)),
                ('license_category', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('b_e', 'B+E'), ('c_e', 'c+E'), ('d_e', 'D+E')], max_length=3)),
                ('is_deleted', models.BooleanField(default=False)),
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
            name='UserLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('uz', 'Uzbek'), ('rus', 'Russia')], max_length=3)),
                ('level', models.CharField(choices=[('il', "Ilg'or"), ('bo', "Boshlang'ich"), ('er', 'Erkin'), ('orta', "O'rta")], max_length=4)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=255)),
                ('work_start_date', models.DateField()),
                ('work_end_date', models.DateField(blank=True, null=True)),
                ('work_now', models.BooleanField(default=False)),
                ('work_duties', models.CharField(blank=True, max_length=500)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
