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
import logging
from django.conf import settings
from django.views.generic import edit
from django.core.urlresolvers import reverse_lazy

logger = logging.getLogger(settings.PROJECT_LOGGER)

class UserForm(forms.ModelForm):
    
    company_name = forms.CharField(label=_("Company Name"))
    web_address  = forms.CharField(label=_("Company Web Address"))
    password1    = forms.CharField(label=_("Enter Password"), widget = forms.PasswordInput)
    password2    = forms.CharField(label=_("Re-enter Password"), widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,) + tuple(User.REQUIRED_FIELDS)
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.user = self.instance
        self.helper = FormHelper()

        logger.debug("Recieved user: " + str(self.user))
        if hasattr(self.user, 'userprofile') == False:
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
        else:
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            
            # Initialise initial values
            self.fields['name'].initial = self.user.name
            profile = self.user.userprofile
            self.fields['company_name'].initial = profile.company_name
            self.fields['web_address'].initial = profile.web_address
            self.fields['email'].initial = self.user.email
            
            self.helper.layout = Layout(
                Field('name', placeholder="Enter Full Name",  autofocus=""),
                Field('company_name', placeholder="Enter Company Name"),
                Field('web_address', placeholder="Enter Company Website Address"),
                Field('email', placeholder="Enter Email", readonly=True),
                Submit('update', 'Update', css_class="btn-warning"),
            )

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2 :
            raise forms.ValidationError("Confirmation password field should match the password")
        return password2.strip()
            
    @transaction.atomic()
    def save(self, commit=True):
        # Override the save method to allow saving user profile as well        
        user = super(UserForm, self).save(commit=False)
        if self.fields['password1'].required == True:
            user.set_password(self.cleaned_data['password1'])

        if commit == True:    
            user.save()
        
        logger.debug("The primary user object saved: " + str(user))

        # Save the user profile linked into this user
        if hasattr(user, 'userprofile') :
            userProfile = user.userprofile
        else:
            userProfile = UserProfile.objects.create(user=user)
            
        userProfile.company_name = self.cleaned_data['company_name']
        userProfile.web_address = self.cleaned_data['web_address']

        if commit == True:
            userProfile.save()

        logger.debug("The user profile got updated: " + str(userProfile))

        # Commit the transaction
        return user

        
