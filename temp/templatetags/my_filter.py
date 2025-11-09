from django import template

register = template.Library()

@register.filter("mobile")
def filter_mobile(content, flag="****"):
    return content[:3]+flag+content[-3:]

@register.filter("sex")
def filter_sex(content):
    return "male" if content == 0 else "female"
