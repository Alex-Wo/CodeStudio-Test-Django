"""
    Кастомный фильтр, для замены разделителя координат объекта с запятой на точку.
    Служит для корректной работы Яндекс.Карты при указании координат в админке.
"""
from django import template

register = template.Library()


@register.filter
def float_format(value):
    if isinstance(value, float):
        return f"{value:.2f}".replace(',', '.')
    return value
