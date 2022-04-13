# Generated by Django 4.0.2 on 2022-04-05 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_image'),
        ('cart', '0002_alter_cart_product_id_alter_cart_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]