"""
Utilities filters which can be used across all application.
"""

from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    """
    Method that add css class in html form_fields
    Usages: {% load pustakalaya_filters %}
            {{ form.subject|addclass:'MyClass' }}
    """
    return value.as_widget(attrs={'class': arg})
