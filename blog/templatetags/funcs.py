#__Author__："汪国强"
#__Date__: 2017/12/6

#####自定义标签
from django import template
from django.utils.safestring import mark_safe

register=template.Library()#register是固定变量名

#filter 参数不能超过两个
@register.filter
def func1(v1,v2):
    return v1+v2
@register.filter
def func2(v1,v2):
    return v1-v2
#simple_tag在html中不能用于if中
@register.simple_tag
def func3(v1,v2):
    return v1*v2