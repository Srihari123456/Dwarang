# Generated by Django 3.0.7 on 2020-06-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta_bill', '0002_auto_20200627_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta_bill',
            name='ticket_no_2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
