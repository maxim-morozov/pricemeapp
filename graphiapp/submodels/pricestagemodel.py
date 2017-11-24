from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings

import logging

logger = logging.getLogger(settings.PROJECT_LOGGER)

class PriceableStageModel:

    # The function to calculate price at this stage
    def calculatePrice(self):
        return 0.0

    # The function to provide indication if this
    # model is priceable or just pre-steps to priceable model
    def isPriceable(self):
        return True

class NonPriceableStageModel:

    # The function to provide indication if this
    # model is priceable or just pre-steps to priceable model
    def isPriceable(self):
        return False
