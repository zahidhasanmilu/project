# Generated by Django 4.0.3 on 2022-03-15 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pid',
        ),
    ]
