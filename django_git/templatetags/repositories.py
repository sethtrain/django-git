from datetime import datetime
import os

from django import template
register = template.Library()
 
@register.filter("name")
def name(value):
    return value.split(os.sep)[-2]

@register.filter("first_eight")
def first_eight(value):
    return "".join(list(str(value))[:8])

@register.filter("tuple_to_date")
def tuple_to_date(value):
    return datetime(value[0], value[1], value[2], value[3], value[4], value[5], value[6])