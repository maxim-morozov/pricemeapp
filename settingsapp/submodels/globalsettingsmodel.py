from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from decimal import Decimal

import logging

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class GlobalSettings(models.Model):

    # The settings need to be linked to the user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Minimum price for all albums which from perspective of the photographer 
    album_minimum_price = models.DecimalField(_('album_minimum_price'), decimal_places=2, default=Decimal(0.0), max_digits=20)

    # Differences between minimum album price visible
    album_minimum_price_difference_visible = models.BooleanField(_('album_minimum_price_difference_visible'), default=False)

    # Percentage on top of the minimum price as photographer price
    commission_percent = models.DecimalField(_('commission_percent'), decimal_places=2, default=Decimal(0.0), max_digits=20)

    # Commission charge visible
    commission_charge_visible = models.BooleanField(_('commission_charge_visible'), default=False)

    # Photographer charge
    photographer_charge = models.DecimalField(_('photographer_charge'), decimal_places=2, default=Decimal(0.0), max_digits=20)
    
    # Photographter charge visible
    photographer_charge_visible = models.BooleanField(_('photographer_charge_visible'), default=False)

    class Meta:
        verbose_name = _('global_settings')
        verbose_name_plural = _('global_settings')
        app_label = 'settingsapp'
