from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg


def sum(value, arg):
    return value + arg
