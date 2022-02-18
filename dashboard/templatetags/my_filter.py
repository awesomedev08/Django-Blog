from django import template

register = template.Library()

@register.filter(name='ro')
def ro(value):
    return range(1, value+1)