# Generated by Django 2.0.7 on 2018-08-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='store/'),
        ),
    ]