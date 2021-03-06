# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accountsin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('reciept', models.CharField(max_length=100)),
                ('bank_acc', models.CharField(max_length=50)),
                ('payment_fees', models.FloatField()),
                ('service_fees', models.FloatField()),
                ('customer_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=10)),
                ('total_fees', models.FloatField()),
                ('remark', models.CharField(max_length=200)),
                ('staff', models.CharField(max_length=50)),
            ],
        ),
    ]
