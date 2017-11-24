from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from .pricestagemodel import NonPriceableStageModel

import logging

logger = logging.getLogger(settings.PROJECT_LOGGER)

class AlbumType(models.Model,
                NonPriceableStageModel):
    
   # The type field
   album_type = models.CharField(max_length=120, default="")

   # The description field
   description = models.CharField(max_length=255, default="")   
        
   class Meta:
       verbose_name = _("album_type")
       verbose_name_plural = _("album_types")
       app_label = 'graphiapp'
    
   def __str__(self):
       return "AlbumType < " + str(self.album_type) + \
              " - " + str(self.description) + " >"
