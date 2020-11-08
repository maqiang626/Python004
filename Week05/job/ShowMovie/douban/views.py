#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04BE9001 maqiang <maqiang626@qq.com> [2020-11-08 20:00 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 1. 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级
# 2. 在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评
#
# ==================================================================
#


from django.shortcuts import render
from django.http import HttpResponse
from .models import TbDouban


def index(request):
    """展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级
    """

    movie_info = TbDouban.objects.filter(star_num__gt=3)
    return render(request, 'index.html', locals())


def search(request):
    """在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评
    """

    search_contents = request.GET.get('q')
    conditions = {'short_comments__icontains': search_contents}
    movie_info = TbDouban.objects.filter(**conditions)
    return render(request, 'index.html', locals())
