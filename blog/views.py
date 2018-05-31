# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

from .models import Author
from .forms import AddForm


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


def add(request):
    a = request.GET['a']
    #a=request.GET.get('a', 0)
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    return render(request, 'home.html')


def home2(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home2.html', {'string': string})


def home3(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home3.html', {'TutorialList': TutorialList})


def home4(request):
    info_dict = {'site': '自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'home4.html', {'info_dict': info_dict})


def home5(request):
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home5.html', {'List': List})


def home6(request):
    return render(request, 'home6.html')


def show_all_data(request):
    result=Author.objects.all()
    return  render(request,'show_all.html',{'all_data':result})


def addform(request):
    return render(request, 'add_form.html')


def post_form(request):  #这个有意思，一个函数同时处理两个请求
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'postform.html', {'form': form})



