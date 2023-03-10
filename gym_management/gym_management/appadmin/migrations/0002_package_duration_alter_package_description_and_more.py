# Generated by Django 4.1.7 on 2023-02-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='Duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='Name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Membership Package'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
