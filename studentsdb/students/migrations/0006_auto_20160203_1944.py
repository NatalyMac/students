# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_exam_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_group',
            field=models.ManyToManyField(to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430'),
        ),
    ]