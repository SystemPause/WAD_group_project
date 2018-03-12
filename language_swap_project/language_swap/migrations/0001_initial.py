# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-11 19:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('LanguageName', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('hobby', models.CharField(blank=True, max_length=500)),
                ('dob', models.DateField(max_length=8, null=True)),
                ('practices', models.ManyToManyField(related_name='practices', to='language_swap.Language')),
                ('speaks', models.ManyToManyField(related_name='speaks', to='language_swap.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='contactedUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacted', to='language_swap.UserProfile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='sourceUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='language_swap.UserProfile'),
        ),
    ]
