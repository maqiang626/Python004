from django.shortcuts import render
from .models import TbSemanticEmotion, TbSentimentAnalysis


def index(request):
    '''采用图表方式展示舆情分析的结果
    '''

    context = common()
    return render(request, 'result.html', context)


def searchk(request):
    """在 Web 界面根据关键字或关键词进行搜索
    """

    context = common()
    search_comment = request.GET.get('qkw')
    conditions = {'comment__icontains': search_comment}
    context['comments'] = TbSemanticEmotion.objects.filter(**conditions)
    return render(request, 'result.html', context)


def searchd(request):
    """按照时间（录入时间）进行搜索
    """

    context = common()
    search_comment = request.GET.get('qdate')
    conditions = {'crawling_date__icontains': search_comment}
    context['comments'] = TbSemanticEmotion.objects.filter(**conditions)
    return render(request, 'result.html', context)


def common():
    '''获取舆情分析的结果
    '''

    # 获取全部评论数据
    comments = TbSemanticEmotion.objects.all()
    counter = TbSemanticEmotion.objects.all().count()

    # 获取舆情分析的结果（最新）
    latest_data = TbSentimentAnalysis.objects.last()
    crawling_date_latest = latest_data.crawling_date_latest
    sentiment_avg = latest_data.sentiment_avg
    plus = latest_data.plus
    minus = latest_data.minus

    context = {
        "comments": comments,
        "counter": counter,
        "crawling_date_latest": crawling_date_latest,
        "sentiment_avg": sentiment_avg,
        "plus": plus,
        "minus": minus
    }

    return context
