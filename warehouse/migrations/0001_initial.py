# Generated by Django 3.0.6 on 2020-05-22 10:52

from django.db import migrations, models
import django.db.models.deletion


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
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Paper_Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.PositiveSmallIntegerField(help_text='format of paper')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Grammage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grammage', models.PositiveSmallIntegerField(help_text='grammage of paper')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='raw material producer company name', max_length=150)),
                ('short_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='paper type name eg: CMP, KLB', max_length=20)),
                ('code', models.CharField(help_text='paper type code eg: K, S, N or Ks', max_length=10)),
                ('description', models.CharField(help_text='paper type description eg: corrugated paper, cellulose', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_id', models.CharField(max_length=120)),
                ('initial_weight', models.PositiveIntegerField()),
                ('current_weight', models.PositiveIntegerField()),
                ('income_date', models.DateTimeField(auto_now_add=True)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Roll_Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Roll')),
            ],
        ),
        migrations.CreateModel(
            name='Roll_Incoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Roll')),
            ],
        ),
        migrations.CreateModel(
            name='Roll_Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Roll')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='company',
            field=models.ForeignKey(help_text='company produced which paper ', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper_Producer'),
        ),
        migrations.AddField(
            model_name='paper',
            name='grammage',
            field=models.ForeignKey(help_text=' paper grammage: 120-145', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper_Grammage'),
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_format',
            field=models.ForeignKey(help_text='paper format: 800-1450', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper_Format'),
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_type',
            field=models.ForeignKey(help_text='paper type: KLB, CMP', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper_Type'),
        ),
    ]
