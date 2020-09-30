# Generated by Django 3.0.7 on 2020-08-25 09:20

from django.db import migrations


def forwards(apps, schema_editor):
    Model = apps.get_model('sales', 'Order')
    for i, obj in enumerate(Model.objects.all()):
        obj.order_id = f'{i}'
        obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ('sales', '0015_order_order_id'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
