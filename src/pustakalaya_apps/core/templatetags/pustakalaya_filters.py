"""
Utilities filters which can be used across all application.
"""

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    """
    Method that add css class in html form_fields
    Usages: {% load pustakalaya_filters %}
            {{ form.subject|addclass:'MyClass' }}
    """
    return value.as_widget(attrs={'class': arg})


@register.filter(name='transtolocal')
@stringfilter
def transtolocal(value):
    """
    """
    from django.utils.translation import get_language
    current_language = get_language()

    ENGLISH_LANGUAGE = ['en-us', 'en-gb', 'en-au', 'en']

    try:
        first =  value.rstrip("]]").split("[[")[0]
    except IndexError:
        first = None

    try:
        second =  value.rstrip("]]").split("[[")[1] or None
        print(second)
    except IndexError:
        second = None


    if current_language in ENGLISH_LANGUAGE and first:
        return first

    if current_language in ENGLISH_LANGUAGE and not first:
        return second or " "

    if current_language not in ENGLISH_LANGUAGE and second:
        return second

    if current_language not in ENGLISH_LANGUAGE and not second:
        return first or " "


@register.filter(name='split')
def split(value, arg):
    return value.split(arg)
