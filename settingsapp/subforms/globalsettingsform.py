from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.urlresolvers import reverse
from django import forms
from django.utils.translation import ugettext_lazy as _
from settingsapp.submodels.globalsettingsmodel import GlobalSettings
from django.db import transaction
import logging
from django.conf import settings
from django.views.generic import edit
from django.core.urlresolvers import reverse_lazy

logger = logging.getLogger(settings.PROJECT_LOGGER)

class GlobalSettingsForm(forms.ModelForm):

    class Meta:
        model = GlobalSettings
        fields = ('album_minimum_price', 'album_minimum_price_difference_visible', 'commission_percent', 'commission_charge_visible', 'photographer_charge', 'photographer_charge_visible')
            
    def __init__(self, *args, **kwargs):
        super(GlobalSettingsForm, self).__init__(*args, **kwargs)
        self.globalsettings = kwargs.get("instance", None)
        logger.debug("Recieved the global settings object: " + str(self.globalsettings))

        # Initialise the fields with the values
        self.fields['album_minimum_price'].initial = self.globalsettings.album_minimum_price
        self.fields['album_minimum_price'].label = _('Album Minimum Price')

        self.fields['album_minimum_price_difference_visible'].initial = self.globalsettings.album_minimum_price_difference_visible
        self.fields['album_minimum_price_difference_visible'].label = _('Show Album Real Price and Album Minimum Price to the Client')

        self.fields['commission_percent'].initial = self.globalsettings.commission_percent
        self.fields['commission_percent'].label = _('Photographer Charge in Percentage %')
        
        self.fields['commission_charge_visible'].initial = self.globalsettings.commission_charge_visible
        self.fields['commission_charge_visible'].label = _('Show Photographer Change (calculated from percentage)')
        
        self.fields['photographer_charge'].initial = self.globalsettings.photographer_charge
        self.fields['photographer_charge'].label = _('Fixed Photographer Charge')
        
        self.fields['photographer_charge_visible'].initial = self.globalsettings.photographer_charge_visible
        self.fields['photographer_charge_visible'].label = _('Show Photographer Fixed Price')
        
        # Initialise the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Field('album_minimum_price',  autofocus=""),
                Field('album_minimum_price_difference_visible'),
                Field('commission_percent'),
                Field('commission_charge_visible'),
                Field('photographer_charge'),
                Field('photographer_charge_visible'),
                Submit('update', 'Update', css_class="btn-warning"))

        @transaction.atomic()
        def save(self, commit=True):
            logger.debug("GlobalSettingsForm saving the new global settings")
            
            globalsettings = super(GlobalSettingsForm, self).save(commit=False)
            
            # Update the fields from the form
            globalsettings.album_minimum_price = self.cleaned_data['album_minimum_price']
            globalsettings.album_minimum_price_difference_visible = self.cleaned_data['album_minimum_price_difference_visible']
            globalsettings.commission_percent = self.cleaned_data['commission_percent']
            globalsettings.commission_charge_visible = self.cleaned_data['commission_charge_visible']
            globalsettings.photographer_charge = self.cleaned_data['photographer_charge']
            globalsettings.photographer_charge_visible = self.cleaned_data['photographer_charge_visible']

            # Commit the changes
            if commit is True:
                globalsettings.save()

            return globalsettings
