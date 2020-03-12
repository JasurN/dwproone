# Generated by Django 3.0.4 on 2020-03-12 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='customer company name', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Measure_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Measurement unit kg or litre or ton', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_amount', models.PositiveIntegerField(help_text='current amount of paper')),
                ('paper_amount_remained_from_last_month', models.PositiveIntegerField(help_text='amount of paper remained from last month')),
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
            name='Paper_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='paper type name eg: CMP, KLB', max_length=20)),
                ('code', models.CharField(help_text='paper type code eg: K, S, N or Ks', max_length=10)),
                ('description', models.CharField(help_text='paper type description eg: corrugated paper, cellulose', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Raw_material_incoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' ', max_length=100)),
                ('amount', models.PositiveIntegerField(help_text=' ')),
                ('amount_remained_from_last_month', models.PositiveIntegerField(help_text=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Raw_Material_Producer_Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='raw material producer company name', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Raw_material_remaining_from_production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' ', max_length=100)),
                ('amount', models.PositiveIntegerField(help_text=' ')),
                ('measurement_id', models.ForeignKey(help_text=' ', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Measure_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Raw_material_consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' ', max_length=100)),
                ('amount', models.PositiveIntegerField(help_text=' ')),
                ('measurement_id', models.ForeignKey(help_text=' ', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Measure_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Raw_material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of raw material vox, bura and etc', max_length=100)),
                ('amount', models.PositiveIntegerField(help_text='current amount of Raw Material')),
                ('amount_remained_from_last_month', models.PositiveIntegerField(help_text='remained from last month amount of Raw Material')),
                ('measurement_id', models.ForeignKey(help_text='foreign key id to measurement', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Measure_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Incoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_income', models.PositiveIntegerField(default=0, help_text='income amount of paper')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paper', models.ForeignKey(default=1, help_text='Paper that is Income', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Income_Remaining_From_Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_income_production', models.PositiveIntegerField(default=0, help_text='income amount of paper from production')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paper', models.ForeignKey(default=1, help_text='Paper that is Income from production', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_consumed', models.PositiveIntegerField(default=0, help_text='consumed amount of paper')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paper', models.ForeignKey(default=1, help_text='Paper that is Consumed', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Paper')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='company',
            field=models.ForeignKey(help_text='company produced which paper ', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Raw_Material_Producer_Company'),
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
        migrations.CreateModel(
            name='Ink_incoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('measurement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Measure_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Ink_consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('measurement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Measure_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Ink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('amount_remained_from_last_month', models.PositiveIntegerField()),
                ('measurement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Measure_unit')),
            ],
        ),
    ]