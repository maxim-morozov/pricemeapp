from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse
from django import forms
from django.utils.translation import ugettext_lazy as _
from authapp.submodels.userprofile import UserProfile
from authtools.models import User
from django.db import transaction

class UserForm(authtoolsforms.UserCreationForm):

    company_name = forms.CharField(label=_("Company Name"))
    web_address  = forms.CharField(label=_("Company Web Address"))
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('name', placeholder="Enter Full Name",  autofocus=""),
            Field('company_name', placeholder="Enter Company Name"),
            Field('web_address', placeholder="Enter Company Website Address"),
            Field('email', placeholder="Enter Email"),
            Field('password1', placeholder="Enter Password"),
            Field('password2', placeholder="Re-enter Password"),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )

    @transaction.atomic()
    def save(self, commit=True):
        # Override the save method to allow saving user profile as well
        user = super(UserForm, self).save(commit=commit)

        # Save the user profile linked into this user  
        userProfile = UserProfile(user = user,
                                  company_name = self.cleaned_data['company_name'],
                                  web_address = self.cleaned_data['web_address'])
        userProfile.save()

        # Commit the transaction
        return user

        
