# Generated by Django 4.1.7 on 2023-03-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0012_product_avg_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_Tag_1',
            field=models.CharField(default='Healthy', max_length=50, verbose_name='First Product Tag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Tag_2',
            field=models.CharField(default='Perfect for dieting', max_length=50, verbose_name='Second Product Tag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Tag_3',
            field=models.CharField(default='Mass Gainer', max_length=50, verbose_name='Third Product Tag'),
            preserve_default=False,
        ),
    ]