# Generated by Django 2.0.7 on 2018-08-22 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20180821_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_for_pad',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]