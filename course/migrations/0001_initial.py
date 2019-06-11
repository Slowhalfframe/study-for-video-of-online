# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 02:51
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
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=99, verbose_name='课程名称')),
                ('course_info', models.TextField(verbose_name='课程简介')),
                ('teacher_info', models.TextField(verbose_name='讲师简介')),
                ('cover_img', models.ImageField(upload_to='static/course/cover', verbose_name='封面图片')),
                ('course', models.FileField(upload_to='static/course/video', verbose_name='课程')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('click_num', models.IntegerField(default=0, verbose_name='播放量')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, verbose_name='课程分类名称')),
                ('info', models.TextField(verbose_name='课程分类介绍')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程分类',
                'verbose_name_plural': '课程分类',
            },
        ),
        migrations.CreateModel(
            name='kejian',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kejian_name', models.CharField(max_length=99, verbose_name='课程名称')),
                ('kejian', models.FileField(blank=True, null=True, upload_to='static/course/kejian', verbose_name='课件')),
            ],
            options={
                'verbose_name': '课件',
                'verbose_name_plural': '课件',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='kj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.kejian', verbose_name='课件'),
        ),
        migrations.AddField(
            model_name='course',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseType', verbose_name='课程分类'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='课程作者'),
        ),
    ]
