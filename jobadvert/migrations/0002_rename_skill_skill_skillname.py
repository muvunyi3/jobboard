# Generated by Django 5.0.3 on 2024-04-20 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobadvert', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='skillName',
        ),
    ]
