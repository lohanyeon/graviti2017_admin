# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class portfolio(models.Model):
    project_kor_name = models.CharField(  # 1. 프로젝트 국문이름
        max_length=200,
        help_text='프로젝트의 한글 이름을 입력하세요',
        verbose_name='프로젝트 국문이름',
    )
    project_eng_name = models.CharField(  # 2. 프로젝트 영문이름
        max_length=200,
        help_text='프로젝트의 영문 이름을 입력하세요',
        verbose_name='프로젝트 영문이름',
    )
    making_year = models.CharField(  # 3. 제작년도
        max_length=4,
        help_text='ex) 2017',
        verbose_name='제작년도',
    )
    making_month = models.CharField(  # 4. 제작월
        max_length=2,
        help_text='ex) 12',
        verbose_name='제작월'
    )

    WEB = 'W1'
    MOBILE = 'M1'
    APP = 'A1'
    VIDEO = 'V1'
    OTHER = 'O1'
    PROJECT_KIND_CHOICES = (
        (WEB, 'Web'),
        (MOBILE, 'Mobile'),
        (APP, 'App'),
        (VIDEO, 'Video'),
        (OTHER, 'Other'),
    )
    project_kind = models.CharField(  # 5. 프로젝트 종류
        max_length=2,
        choices=PROJECT_KIND_CHOICES,
        default=WEB,
        help_text='프로젝트 종류를 선택하세요',
        verbose_name='프로젝트 종류',
    )

    project_summary = models.TextField(  # 6. 프로젝트 요약
        max_length=1000,
        help_text='프로젝트 요약을 입력하세요',
        verbose_name='프로젝트 요약',
    )
    project_period = models.CharField(  # 7. 프로젝트 기간
        max_length=30,
        help_text='ex) 2017.01 ~ 2017.12',
        verbose_name='프로젝트 기간',
    )
    project_range = models.CharField(  # 8. 프로젝트 범위
        max_length=500,
        help_text='',
        verbose_name='프로젝트 범위',
    )
    client_name = models.CharField(  # 9. 고객사 이름
        max_length=100,
        help_text='',
        verbose_name='고객사 이름',
    )
    producer = models.CharField(  # 10. 제작사 이름
        max_length=100,
        help_text='',
        verbose_name='제작사 이름',
    )
    bg_image_horizontal = models.ImageField(  # 11. 백그라운드 이미지 가로형
        upload_to='images/%Y%m%d',
        null=True,
        help_text='PC에서 사용 할 배경이미지 - width, height지정필요',
        verbose_name='백그라운드 이미지(가로형)',
        max_length=200,
    )
    bg_image_vertical = models.ImageField(  # 11. 백그라운드 이미지 세로형
        upload_to='images/%Y%m%d',
        null=True,
        help_text='MOBILE에서 사용 할 배경 이미지 - width, height지정필요',
        verbose_name='백그라운드 이미지(세로형)',
        max_length=200,
    )
    thumb_image = models.ImageField(  # 12. 썸네일이미지
        upload_to='images/%Y%m%d',
        null=True,
        help_text='width, height지정필요',
        verbose_name='썸네일 이미지',
        max_length=200,
    )
    main_image = models.ImageField(  # 13. 메인이미지
        upload_to='images/%Y%m%d',
        null=True,
        help_text='width, height지정필요',
        verbose_name='메인 이미지',
    )
    sub_image01 = models.ImageField(  # 14. 서브이미지01
        upload_to='images/%Y%m%d',
        null=True,
        help_text='--',
        verbose_name='서브 이미지01',
    )
    sub_image02 = models.ImageField(  # 15. 서브이미지02
        upload_to='images/%Y%m%d',
        null=True,
        help_text='--',
        verbose_name='서브 이미지02',
    )
    sub_image03 = models.ImageField(  # 16. 서브이미지03
        upload_to='images/%Y%m%d',
        null=True,
        help_text='--',
        verbose_name='서브 이미지03',
    )
    sub_image04 = models.ImageField(  # 17. 서브이미지04
        upload_to='images/%Y%m%d',
        null=True,
        help_text='--',
        verbose_name='서브 이미지04',
    )
    icon_image = models.ImageField(  # 18. 아이콘이미지
        upload_to='images/%Y%m%d',
        null=True,
        help_text='--',
        verbose_name='아이콘 아미지',
    )
    mobile_image = models.ImageField(  # 19. 모바일이미지
        upload_to='images/%Y%m%d',
        null=True,
        help_text='--',
        verbose_name='모바일 이미지',
    )
    video_url = models.TextField(  # 20. 영상URL
        null=True,
        help_text='vimeo영상 url소스를 입력하세요',
        verbose_name='영상 URL',
    )

    OPEN = 'Y'
    NOTOPEN = 'N'
    OPEN_YN_CHOICE = (
        (OPEN, '공개'),
        (NOTOPEN, '비공개'),
    )
    open_yn = models.CharField(  # 21. 공개여부
        max_length=1,
        null=False,
        choices=OPEN_YN_CHOICE,
        default=OPEN,
        help_text='',
        verbose_name='공개여부',
    )

    show_order = models.IntegerField(  # 22. 노출순서
        null=False,
        help_text='ex) 10',
        verbose_name='노출순서',
    )
    reg_date = models.DateField(  # 23. 등록일자
        auto_now_add=False,
        help_text='오늘일자 또는 원하는 일자를 선택하세요',
        verbose_name='등록일자',
    )

    class Meta:
        verbose_name = "포토폴리오"
        verbose_name_plural = "포토폴리오"

    def __unicode__(self):
        return self.project_kor_name
