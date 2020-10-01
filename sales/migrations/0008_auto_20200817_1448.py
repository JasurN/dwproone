# Generated by Django 3.0.7 on 2020-08-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_orderdelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='corrugator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='flex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='glue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='stitching',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='thompson',
            field=models.BooleanField(default=False),
        ),
    ]