from django.conf import settings
from django.contrib.auth import get_user_model
from braces import views as bracesviews
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from graphiapp.submodels.albumtypemodel import AlbumType
from graphiapp.subforms.albumtypeform import AlbumTypeForm

import logging

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class AlbumTypeView(bracesviews.LoginRequiredMixin,
                    generic.DetailView,
                    generic.edit.FormMixin):

    model = AlbumType
    template_name = "albumtypes.html"
    login_url = reverse_lazy('login')
    form_class = AlbumTypeForm
    
    def get_object(self, queryset=None):
        pass
