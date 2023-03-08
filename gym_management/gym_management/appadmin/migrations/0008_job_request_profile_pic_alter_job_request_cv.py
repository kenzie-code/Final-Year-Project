# Generated by Django 4.1.7 on 2023-03-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0007_job_request_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_request',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='media/job_request/profilepic/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_request',
            name='cv',
            field=models.FileField(upload_to='media/job_request/cv/', verbose_name='CV'),
        ),
    ]