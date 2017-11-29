"""
Utilities filters which can be used across all application.
"""

from django import template
from django.template.defaultfilters import stringfilter
from pustakalaya_apps.core.constants import LANGUAGES_DICT as languages
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
import os

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
        first = value.rstrip("]]").split("[[")[0]
    except IndexError:
        first = None

    try:
        second = value.rstrip("]]").split("[[")[1] or None
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


@register.filter(name='cast')
def split(value, type):
    try:
        return type(value)
    except ValueError:
        return value


@register.filter(name='get_language')
def get_language(language_code):
    return languages.get(language_code)


@register.filter(name='slugify_unicode')
def slugify_unicode(value):
    return slugify(value, allow_unicode=True)

@register.filter(name='file_size_format')
def file_size_format(value):
    """
    Simple kb/mb/gb size snippet for templates:

    {{ product.file.size|sizify }}
    """
    # value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = _("KB")
    elif value < 4194304000:
        value = value / 1048576.0
        ext = _("MB")
    else:
        value = value / 1073741824.0
        ext = _("GB")
    return '%s %s' % (str(round(value, 2)), ext)

