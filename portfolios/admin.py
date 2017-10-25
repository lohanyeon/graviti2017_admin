# -*- coding: utf-8 -*-

from django.contrib import admin
from portfolios.models import portfolio


class portfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('프로젝트 기본정보', {
            'fields': [
                'project_kor_name',
                'project_eng_name',
                'making_year',
                'making_month',
                'project_kind',
                'project_summary',
                'project_period',
                'project_range',
                'client_name',
                'producer',
            ]
        }),
        ('프로젝트 이미지', {
            'fields': [
                'bg_image_horizontal',
                'bg_image_vertical',
                'thumb_image',
                'main_image',
                'sub_image01',
                'sub_image02',
                'sub_image03',
                'sub_image04',
                'icon_image',
                'mobile_image',
            ]
        }),
        ('영상 프로젝트', {
            'fields': [
                'video_url',
            ]
        }),
        ('사용자화면 제어', {
            'fields': [
                'open_yn',
                'show_order',
                'reg_date',
            ]
        }),
    ]
    list_display = (
        'project_kor_name',
        'making_year',
        'project_kind',
        'client_name',
        'project_period',
        'open_yn',
        'show_order',
        'reg_date',
    )
    list_filter = [
        'open_yn',
        'client_name',
    ]
    search_fields = [
        'project_kor_name',
        'project_eng_name',
        'client_name',
    ]


# Register your models here.
admin.site.register(portfolio, portfolioAdmin)
