# Generated by Django 3.0.7 on 2020-07-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert_a', '0004_auto_20200702_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cert_a',
            name='Consult_dt2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Consult_fee2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='DiagTest_center2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='DiagTest_name2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Diagnostic_Test_price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Injection_fee2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Med_CashMemoNo2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Med_name2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cert_a',
            name='Quantity2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
