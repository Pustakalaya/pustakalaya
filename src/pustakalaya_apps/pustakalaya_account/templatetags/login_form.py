from django import template
from pustakalaya_apps.pustakalaya_account.login_form import LoginForm

register = template.Library()


@register.inclusion_tag('_partials/login_form.html')
def login_form():
    return {'form': LoginForm(),
            'signup_url': '/accounts/signup/'
            }
