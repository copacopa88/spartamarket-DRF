# Generated by Django 4.2 on 2024-05-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_gender_alter_user_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='default.png', upload_to='profile/'),
        ),
    ]