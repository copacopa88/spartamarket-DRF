# Generated by Django 4.2 on 2024-04-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='product',
            name='like_users',
        ),
    ]
