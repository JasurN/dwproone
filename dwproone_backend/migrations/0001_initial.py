# Generated by Django 3.0.4 on 2020-03-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaperConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaperFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.PositiveIntegerField(verbose_name='format of paper')),
            ],
        ),
        migrations.CreateModel(
            name='PaperGrammage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grammage', models.PositiveIntegerField(verbose_name='grammage of paper')),
            ],
        ),
        migrations.CreateModel(
            name='PaperIncomeRemainingFromProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaperIncoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaperType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='paper type name eg: CMP, KLB')),
                ('code', models.CharField(max_length=10, verbose_name='paper type code eg: K, S, N or Ks')),
                ('description', models.CharField(max_length=100,
                                                 verbose_name='paper type description eg: corrugated paper, cellulose')),
            ],
        ),
    ]
