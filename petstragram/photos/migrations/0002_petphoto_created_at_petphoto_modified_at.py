# Generated by Django 5.0.2 on 2024-02-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petphoto',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
