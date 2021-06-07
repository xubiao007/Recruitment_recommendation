from django.shortcuts import render


# 首页提示
def home_tip(request):
    message = '请先登陆平台！'
    return render(request, 'index.html', locals())



