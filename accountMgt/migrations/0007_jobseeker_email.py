# Generated by Django 5.0.3 on 2024-04-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountMgt', '0006_recruiter_email_alter_jobseeker_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='email',
            field=models.CharField(default='', max_length=25),
        ),
    ]
