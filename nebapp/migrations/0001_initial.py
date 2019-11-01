# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-31 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=40)),
                ('business_description', tinymce.models.HTMLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Joining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField()),
                ('location', models.CharField(choices=[('Kicukiro', 'Kicukiro'), ('Remera', 'Remera'), ('Gatenga', 'Gatenga'), ('Gisozi', 'Gisozi'), ('Kacyiru', 'Kacyiru'), ('Karuruma', 'Karuruma'), ('Gatsata', 'Gatsata'), ('Nyamirambo', 'Nyamirambo'), ('Nyamata', 'Nyamata'), ('Huye', 'Huye'), ('Gisenyi', 'Gisenyi'), ('Kibuye', 'Kibuye')], max_length=40)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('police_contact', models.IntegerField(default='112')),
                ('hospital_contact', models.IntegerField(default='911')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=80)),
                ('post', tinymce.models.HTMLField()),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebapp.Neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', tinymce.models.HTMLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hood', models.OneToOneField(blank=True, default='Kigali', null=True, on_delete=django.db.models.deletion.CASCADE, to='nebapp.Neighbourhood')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='joining',
            name='hood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebapp.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='joining',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nebapp.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
