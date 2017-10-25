# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-08 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_kor_name', models.CharField(max_length=200)),
                ('project_eng_name', models.CharField(max_length=200)),
                ('making_year', models.CharField(max_length=4)),
                ('making_month', models.CharField(max_length=2)),
                ('project_kind', models.CharField(choices=[('W1', 'Web'), ('M1', 'Mobile'), ('A1', 'App'), ('V1', 'Video'), ('O1', 'Other')], default='W1', max_length=2)),
                ('project_summary', models.CharField(max_length=1000)),
                ('project_period', models.CharField(max_length=30)),
                ('project_range', models.CharField(max_length=500)),
                ('client_name', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('bg_image', models.ImageField(help_text='width, height\uc9c0\uc815\ud544\uc694', max_length=200, upload_to='images/%Y%m%d', verbose_name='\ubc31\uadf8\ub77c\uc6b4\ub4dc\uc774\ubbf8\uc9c0')),
                ('thumb_image', models.ImageField(help_text='width, height\uc9c0\uc815\ud544\uc694', max_length=200, upload_to='images/%Y%m%d', verbose_name='\uc378\ub124\uc77c\uc774\ubbf8\uc9c0')),
                ('main_image', models.ImageField(help_text='width, height\uc9c0\uc815\ud544\uc694', upload_to='images/%Y%m%d', verbose_name='\uba54\uc778\uc774\ubbf8\uc9c0')),
                ('sub_image01', models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='\uc11c\ube0c\uc774\ubbf8\uc9c001')),
                ('sub_image02', models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='\uc11c\ube0c\uc774\ubbf8\uc9c002')),
                ('sub_image03', models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='\uc11c\ube0c\uc774\ubbf8\uc9c003')),
                ('sub_image04', models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='\uc11c\ube0c\uc774\ubbf8\uc9c004')),
                ('icon_image', models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='\uc544\uc774\ucf58 \uc544\ubbf8\uc9c0')),
                ('mobile_image', models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='\ubaa8\ubc14\uc77c\uc774\ubbf8\uc9c0')),
                ('video_url', models.CharField(max_length=1000, null=True)),
                ('open_yn', models.CharField(choices=[('Y', '\uacf5\uac1c'), ('N', '\ube44\uacf5\uac1c')], default='Y', max_length=1)),
                ('show_order', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\ud3ec\ud1a0\ud3f4\ub9ac\uc624',
                'verbose_name_plural': '\ud3ec\ud1a0\ud3f4\ub9ac\uc624',
            },
        ),
        migrations.DeleteModel(
            name='portfolios',
        ),
    ]
