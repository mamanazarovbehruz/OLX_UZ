# Generated by Django 4.1.6 on 2023-02-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productfield_is_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]
