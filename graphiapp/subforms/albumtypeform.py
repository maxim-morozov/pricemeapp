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

import logging

logger = logging.getLogger(settings.PROJECT_LOGGER)

class AlbumTypeForm(forms.Form):

    album_type = forms.ChoiceField(widget=forms.Select(), required=True)
    
    class Meta:
        fields = ('album_type',)

    def __init__(self, *args, **kwargs):
        kwargs.pop("instance", None)
        self.types = kwargs.pop("types", None)
        super(AlbumTypeForm, self).__init__(*args, **kwargs)
        

        logger.debug("AlbumTypeForm: Initialising the form with " + str(self.types))

        self.fields["album_type"].choices = [(l.album_type, l.description) for l in self.types]
        self.fields["album_type"].label = _('Choose Album Type')
        
        # Initialise the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('album_type', autofocus=True),
            Submit('next', 'Next', css_class="btn-warning"))
