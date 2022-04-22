# Generated by Django 4.0.2 on 2022-04-11 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc_api', '0011_file_remove_project_draft_draw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_detail', to='calc_api.customer'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='stuff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_detail', to='calc_api.staff'),
        ),
    ]