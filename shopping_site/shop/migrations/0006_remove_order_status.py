# Generated by Django 5.1.1 on 2024-09-21 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_stauts_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
