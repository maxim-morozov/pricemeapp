from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from .usermanager import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    email = models.EmailField(_('Email address'), unique=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=True)
    company_name = models.CharField(_('Company'), max_length=120, blank=True)
    web_address = models.CharField(_('Web address'), max_length=120, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company_name', 'web_address']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        app_label = 'authapp'

    def get_full_name(self):
        """ Returns the full name of the user which is combined from first name and second name fields """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Returns short name of the user which is just their first name """
        return self.first_name

    def email_user(self, subject, message, from_email, **kwargs):
        """ Sends the email to the user """
        send_mail(subject, message, from_email, **kwargs)
        
