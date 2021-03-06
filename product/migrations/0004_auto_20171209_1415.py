# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-09 14:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20171209_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
