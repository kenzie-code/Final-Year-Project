# Generated by Django 4.1.7 on 2023-02-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_headline_cards_alter_cards_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline_cards',
            name='short_description',
            field=models.CharField(max_length=250, verbose_name='Short Description'),
        ),
    ]