# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-09 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_auto_20170808_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='bg_image',
            field=models.ImageField(help_text='width, height\uc9c0\uc815\ud544\uc694', max_length=200, upload_to='images/%Y%m%d', verbose_name='11. \ubc31\uadf8\ub77c\uc6b4\ub4dc \uc774\ubbf8\uc9c0'),
        ),
        migrations.AlterField(
            model_name='list',
            name='client_name',
            field=models.CharField(max_length=100, verbose_name='9. \uace0\uac1d\uc0ac \uc774\ub984'),
        ),
        migrations.AlterField(
            model_name='list',
            name='icon_image',
            field=models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='18. \uc544\uc774\ucf58 \uc544\ubbf8\uc9c0'),
        ),
        migrations.AlterField(
            model_name='list',
            name='main_image',
            field=models.ImageField(help_text='width, height\uc9c0\uc815\ud544\uc694', upload_to='images/%Y%m%d', verbose_name='13. \uba54\uc778 \uc774\ubbf8\uc9c0'),
        ),
        migrations.AlterField(
            model_name='list',
            name='making_month',
            field=models.CharField(help_text='ex) 12', max_length=2, verbose_name='4. \uc81c\uc791\uc6d4'),
        ),
        migrations.AlterField(
            model_name='list',
            name='making_year',
            field=models.CharField(help_text='ex) 2017', max_length=4, verbose_name='3. \uc81c\uc791\ub144\ub3c4'),
        ),
        migrations.AlterField(
            model_name='list',
            name='mobile_image',
            field=models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='19. \ubaa8\ubc14\uc77c \uc774\ubbf8\uc9c0'),
        ),
        migrations.AlterField(
            model_name='list',
            name='open_yn',
            field=models.CharField(choices=[('Y', '\uacf5\uac1c'), ('N', '\ube44\uacf5\uac1c')], default='Y', max_length=1, verbose_name='21. \uacf5\uac1c\uc5ec\ubd80'),
        ),
        migrations.AlterField(
            model_name='list',
            name='producer',
            field=models.CharField(max_length=100, verbose_name='10. \uc81c\uc791\uc0ac \uc774\ub984'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project_eng_name',
            field=models.CharField(help_text='\ud504\ub85c\uc81d\ud2b8\uc758 \uc601\ubb38 \uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694', max_length=200, verbose_name='2. \ud504\ub85c\uc81d\ud2b8 \uc601\ubb38\uc774\ub984'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project_kind',
            field=models.CharField(choices=[('W1', 'Web'), ('M1', 'Mobile'), ('A1', 'App'), ('V1', 'Video'), ('O1', 'Other')], default='W1', help_text='\ud504\ub85c\uc81d\ud2b8 \uc885\ub958\ub97c \uc120\ud0dd\ud558\uc138\uc694', max_length=2, verbose_name='5. \ud504\ub85c\uc81d\ud2b8 \uc885\ub958'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project_kor_name',
            field=models.CharField(help_text='\ud504\ub85c\uc81d\ud2b8\uc758 \ud55c\uae00 \uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694', max_length=200, verbose_name='1. \ud504\ub85c\uc81d\ud2b8 \uad6d\ubb38\uc774\ub984'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project_period',
            field=models.CharField(help_text='ex) 2017.01 ~ 2017.12', max_length=30, verbose_name='7. \ud504\ub85c\uc81d\ud2b8 \uae30\uac04'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project_range',
            field=models.CharField(max_length=500, verbose_name='8. \ud504\ub85c\uc81d\ud2b8 \ubc94\uc704'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project_summary',
            field=models.TextField(help_text='\ud504\ub85c\uc81d\ud2b8 \uc694\uc57d\uc744 \uc785\ub825\ud558\uc138\uc694', max_length=1000, verbose_name='6. \ud504\ub85c\uc81d\ud2b8 \uc694\uc57d'),
        ),
        migrations.AlterField(
            model_name='list',
            name='reg_date',
            field=models.DateField(help_text='\uc624\ub298\uc77c\uc790 \ub610\ub294 \uc6d0\ud558\ub294 \uc77c\uc790\ub97c \uc120\ud0dd\ud558\uc138\uc694', verbose_name='23. \ub4f1\ub85d\uc77c\uc790'),
        ),
        migrations.AlterField(
            model_name='list',
            name='show_order',
            field=models.IntegerField(help_text='ex) 10', verbose_name='22. \ub178\ucd9c\uc21c\uc11c'),
        ),
        migrations.AlterField(
            model_name='list',
            name='sub_image01',
            field=models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='14. \uc11c\ube0c \uc774\ubbf8\uc9c001'),
        ),
        migrations.AlterField(
            model_name='list',
            name='sub_image02',
            field=models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='15. \uc11c\ube0c \uc774\ubbf8\uc9c002'),
        ),
        migrations.AlterField(
            model_name='list',
            name='sub_image03',
            field=models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='16. \uc11c\ube0c \uc774\ubbf8\uc9c003'),
        ),
        migrations.AlterField(
            model_name='list',
            name='sub_image04',
            field=models.ImageField(help_text='--', null=True, upload_to='images/%Y%m%d', verbose_name='17. \uc11c\ube0c \uc774\ubbf8\uc9c004'),
        ),
        migrations.AlterField(
            model_name='list',
            name='thumb_image',
            field=models.ImageField(help_text='width, height\uc9c0\uc815\ud544\uc694', max_length=200, upload_to='images/%Y%m%d', verbose_name='12. \uc378\ub124\uc77c \uc774\ubbf8\uc9c0'),
        ),
        migrations.AlterField(
            model_name='list',
            name='video_url',
            field=models.CharField(help_text='vimeo\uc601\uc0c1 url\uc18c\uc2a4\ub97c \uc785\ub825\ud558\uc138\uc694', max_length=1000, null=True, verbose_name='20. \uc601\uc0c1 URL'),
        ),
    ]
