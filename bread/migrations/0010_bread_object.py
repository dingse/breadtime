# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bread', '0009_auto_20160303_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bread_object',
            fields=[
                ('bread_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bread.Bread')),
            ],
            bases=('bread.bread',),
        ),
    ]
