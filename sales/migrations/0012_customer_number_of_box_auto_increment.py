# Generated by Django 3.0.7 on 2020-08-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_auto_20200825_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='number_of_box_auto_increment',
            field=models.IntegerField(default=0),
        ),
    ]
