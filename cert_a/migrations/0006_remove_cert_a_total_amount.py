# Generated by Django 3.0.7 on 2020-07-05 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cert_a', '0005_auto_20200702_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cert_a',
            name='Total_amount',
        ),
    ]