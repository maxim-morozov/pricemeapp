from django.db import models
from authtools.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):

    # Link to the user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # User information fields
    company_name = models.CharField(_('company_name'), max_length=120, blank=True)
    web_address = models.CharField(_('web_address'), max_length=120, blank=True)

    class Meta:
        verbose_name = _('user_profile')
        verbose_name_plural = _('users_profiles')
        app_label = 'authapp'

    def get_company_name(self):
        return self.company_name

    def get_web_address(self):
        return self.web_address

    

    
