# Generated by Django 4.0.3 on 2022-03-08 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_product_id_alter_product_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pid',
        ),
    ]