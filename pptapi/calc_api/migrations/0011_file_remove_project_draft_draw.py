# Generated by Django 4.0.2 on 2022-04-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_api', '0010_remove_customer_phone_remove_staff_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('body', models.BinaryField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='draft_draw',
        ),
    ]
