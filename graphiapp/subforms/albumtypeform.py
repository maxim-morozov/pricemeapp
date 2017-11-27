from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.urlresolvers import reverse
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.views.generic import edit
from django.core.urlresolvers import reverse_lazy
from graphiapp.submodels.albumtypemodel import AlbumType

import logging

logger = logging.getLogger(settings.PROJECT_LOGGER)

class AlbumTypeForm(forms.ModelForm):

    album_type = forms.ChoiceField(widget=forms.Select(), required=True)
    
    class Meta:
        fields = ('album_type',)
        model = AlbumType

    def __init__(self, *args, **kwargs):
        #kwargs.pop("instance", None)
        super(AlbumTypeForm, self).__init__(*args, **kwargs)
        self.types = AlbumType.objects.all()

        logger.debug("AlbumTypeForm: Initialising the form with " + str(self.types))

        self.fields["album_type"].choices = [(l.album_type, l.description) for l in self.types]
        self.fields["album_type"].label = _('Choose Album Type')
        
        # Initialise the layout
        self.helper = FormHelper()
        #self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('album_type', autofocus=""))
