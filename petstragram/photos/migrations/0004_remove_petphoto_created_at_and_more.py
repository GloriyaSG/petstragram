# Generated by Django 5.0.2 on 2024-02-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_petphoto_pets_alter_petphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petphoto',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='petphoto',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='petphoto',
            name='date_of_publication',
            field=models.DateField(auto_now=True),
        ),
    ]