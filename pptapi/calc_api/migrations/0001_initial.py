# Generated by Django 4.0.2 on 2022-02-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=50)),
                ('price_inc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_out', models.DecimalField(decimal_places=2, max_digits=10)),
                ('install_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('install_time', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc_api.vendor')),
            ],
        ),
    ]