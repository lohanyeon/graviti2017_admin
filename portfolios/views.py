# coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.views.generic import TemplateView, ListView, DetailView
from portfolios.models import portfolio
from django.db.models import Max, Min
from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)


class Portfolio(ListView):
    queryset = portfolio.objects.all().order_by('-show_order')
    model = queryset.filter(open_yn='Y')


def json_portfolio_list(request):
    queryset = portfolio.objects.all().order_by('-show_order')
    portfolio_list = queryset.filter(open_yn='Y')

    print 'json_portfolio_list'

    data = serializers.serialize('json', portfolio_list)

    return HttpResponse(data, 'application/json')


def json_portfolio_by_pk(request, pk):
    queryset = portfolio.objects.all()
    next = queryset.filter(pk__gt=pk).aggregate(Max('id'))
    prev = queryset.filter(pk__lt=pk).aggregate(Min('id'))

    print next.get('id__max')
    print prev.get('id__min')

    next_id = next.get('id__max')
    prev_id = prev.get('id__min')

    # 이전/다음 게시물 쿼리 리턴 결과가 없을때 serializers.seralize에 null상태로 대입하면 에러발생함
    # 어떻게 처리해야할지 난감하여(널 처리를) 이전/다음 아이디가 없을경우는 현재 아이디로 대체함
    # 즉 이전 다음 아이디가 현재 아이디와 같다면 이전 또는 다음 게시물이 없다는 뜻
    if next_id:
        next_obj = portfolio.objects.get(pk=next_id)
        print next_obj
    else:
        next_obj = portfolio.objects.get(pk=pk)

    if prev_id:
        prev_obj = portfolio.objects.get(pk=prev_id)
    else:
        prev_obj = portfolio.objects.get(pk=pk)

    obj = portfolio.objects.get(pk=pk)
    data = serializers.serialize('json', [obj, ])
    try:
        data = serializers.serialize('json', [obj, prev_obj, next_obj])
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))

    return HttpResponse(data, 'application/json')


def get_next_or_prev(models, item, direction):
    getit = False

    if direction == 'prev':
        models = models.reverse()
    for m in models:
        if getit:
            return m
        if item == m:
            getit = True
    if getit:
        return models[0]
    return False
