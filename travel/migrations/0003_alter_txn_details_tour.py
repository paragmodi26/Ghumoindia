# Generated by Django 3.2 on 2021-06-22 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_txn_details_tour_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='txn_details',
            name='tour',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='travel.add_tour'),
        ),
    ]
