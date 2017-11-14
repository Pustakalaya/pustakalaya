from allauth.account.forms import LoginForm
class PustakalayaLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(PustakalayaLoginForm, self).__init__(*args, **kwargs)
        self.fields['remember'].label = 'Stay signed in'
        self.fields['remember'].initial = False
