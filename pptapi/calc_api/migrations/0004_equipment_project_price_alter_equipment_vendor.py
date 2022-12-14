# Generated by Django 4.0.2 on 2022-02-21 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc_api', '0003_alter_equipment_jsname'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='project_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='calc_api.vendor'),
        ),
    ]
