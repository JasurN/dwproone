# Generated by Django 3.0.7 on 2020-08-25 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0020_auto_20200825_1514'),
        ('production', '0002_production_production_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Order'),
        ),
    ]
