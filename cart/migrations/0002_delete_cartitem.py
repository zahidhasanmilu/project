# Generated by Django 4.0.3 on 2022-03-09 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cartItem',
        ),
    ]