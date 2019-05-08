from django.shortcuts import render
from .models import Info


def info_list(request):
    # DB로부터 모든 Item List를 가져올 예정
    qs = Info.objects.all()  # QuerySet 타입
    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'myintro/info_list.html', {
        'info_list': qs,
    })


def info_detail(request, pk):
    info = Info.objects.get(pk=pk)  # 즉시 DB로부터 Fetch
    return render(request, 'myintro/info_detail.html', {
        'info': info,
    })


