# Generated by Django 5.1.1 on 2024-09-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=225),
        ),
    ]
