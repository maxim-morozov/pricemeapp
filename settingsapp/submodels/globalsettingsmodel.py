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
    album_minimum_price = models.DecimalField(decimal_places=2, default=Decimal(0.0), max_digits=20)

    # Differences between minimum album price visible
    album_minimum_price_difference_visible = models.BooleanField(default=False)

    # Percentage on top of the minimum price as photographer price
    commission_percent = models.DecimalField(decimal_places=2, default=Decimal(0.0), max_digits=20)

    # Commission charge visible
    commission_charge_visible = models.BooleanField(default=False)

    # Photographer charge
    photographer_charge = models.DecimalField(decimal_places=2, default=Decimal(0.0), max_digits=20)
    
    # Photographter charge visible
    photographer_charge_visible = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('global_settings')
        verbose_name_plural = _('global_settings')
        app_label = 'settingsapp'

    def __str__(self):
        return "GlobalSettings < user: " + str(self.user) + ", album_minimum_price: " + str(self.album_minimum_price) + ", album_minimum_price_difference_visible: " + str(self.album_minimum_price_difference_visible) + ", commission_percent: " + str(self.commission_percent) + ", commission_charge_visible: " + str(self.commission_charge_visible) + ", photographer_charge: " + str(self.photographer_charge) + ", photographer_charge_visible: " + str(self.photographer_charge_visible) + " > "
