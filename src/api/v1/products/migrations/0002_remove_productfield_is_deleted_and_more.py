# Generated by Django 4.1.6 on 2023-02-15 16:17

import api.v1.accounts.services
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfield',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='productfield',
            name='is_main',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=api.v1.accounts.services.upload_category_path),
        ),
        migrations.AddField(
            model_name='field',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=9000, validators=[django.core.validators.MinLengthValidator(80)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='Raqam 13 ta belgidan iborat bolishi kerak. P.s: +998912345678', regex='^\\+?998?\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='productfield',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.field'),
        ),
        migrations.AlterField(
            model_name='productfield',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_fields', to='products.product'),
        ),
    ]