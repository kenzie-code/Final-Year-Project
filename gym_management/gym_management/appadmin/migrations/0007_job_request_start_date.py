# Generated by Django 4.1.7 on 2023-03-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0006_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_request',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]