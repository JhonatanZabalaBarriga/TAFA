# Generated by Django 4.1.dev20220419042538 on 2022-08-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='asset_id',
            field=models.CharField(default='replace', max_length=250, primary_key=True, serialize=False),
        ),
    ]
