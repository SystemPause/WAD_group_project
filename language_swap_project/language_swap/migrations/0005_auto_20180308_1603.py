# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language_swap', '0004_auto_20180308_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Speaks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='language',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='practices',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='speaks',
        ),
        migrations.AlterField(
            model_name='language',
            name='LanguageName',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='speaks',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakerLanguage', to='language_swap.Language'),
        ),
        migrations.AddField(
            model_name='speaks',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakerName', to='language_swap.UserProfile'),
        ),
        migrations.AddField(
            model_name='practices',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practicelanguage', to='language_swap.Language'),
        ),
        migrations.AddField(
            model_name='practices',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practiceName', to='language_swap.UserProfile'),
        ),
    ]
