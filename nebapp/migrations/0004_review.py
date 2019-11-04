# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-03 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nebapp', '0003_auto_20191103_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.IntegerField(blank=True, default=0)),
                ('average_review', models.IntegerField(blank=True, default=0)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebapp.Neighbourhood')),
                ('judge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]