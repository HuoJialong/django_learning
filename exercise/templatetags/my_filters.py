from django import template
register = template.Library()

@register.filter("toFixed")
def toFixed(value, len = 2):
    return f"{value:.{len}f}"
