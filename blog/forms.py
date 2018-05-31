# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 23:13
# @Author  : sundongjian
# @Email   : xiaobomentu@163.com
# @File    : forms.py.py
# @Software: PyCharm


from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()