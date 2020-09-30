# Generated by Django 3.0.7 on 2020-08-17 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20200812_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.Order')),
            ],
        ),
    ]
