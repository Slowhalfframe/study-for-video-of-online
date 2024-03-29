# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 03:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
