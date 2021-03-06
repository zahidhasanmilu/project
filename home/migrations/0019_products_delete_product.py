# Generated by Django 4.0.3 on 2022-03-09 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_product_id_product_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='media/producct/')),
                ('delivery', models.SmallIntegerField(default='3')),
                ('quantiles', models.SmallIntegerField(default='1')),
                ('stock', models.BooleanField(default=True)),
                ('catagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.catagory')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
