from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(AuthenticationForm):
    #username = forms.CharField(label = _('Username'), required=True)
    #password = forms.CharField(widget = forms.PasswordInput(), label = _('Password'), required=True) 
    remember_me = forms.BooleanField(required=False, initial=False)

    #class Meta:
        #model = User
    #    fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Enter Email", autofocus=""),
            Field('password', placeholder="Enter Password"),
            # TODO - provide ability to reset password
            #HTML('<a href="{}">Forgot Password?</a>'.format(
            #    reverse("accounts:password-reset"))),
            Field('remember_me'),
            Submit('sign_in', 'Log in',
                   css_class="btn btn-lg btn-primary btn-block"),
            )
