# Generated by Django 3.0.7 on 2020-08-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20200825_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='production_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]