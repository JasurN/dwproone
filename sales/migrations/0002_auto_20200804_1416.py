# Generated by Django 3.0.7 on 2020-08-04 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id']},
        ),
    ]
