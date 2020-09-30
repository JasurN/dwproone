# Generated by Django 3.0.7 on 2020-08-25 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0020_auto_20200825_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Order'),
        ),
    ]
