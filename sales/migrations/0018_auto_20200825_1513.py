# Generated by Django 3.0.7 on 2020-08-25 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0017_auto_20200825_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Box'),
        ),
    ]
