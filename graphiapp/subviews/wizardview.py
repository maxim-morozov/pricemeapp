from django.conf import settings
from django.contrib.auth import get_user_model
from braces import views as bracesviews
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from graphiapp.submodels.albumtypemodel import AlbumType
from graphiapp.subforms.albumtypeform import AlbumTypeForm
from formtools.wizard.views import SessionWizardView

import logging

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class WizardView(bracesviews.LoginRequiredMixin,
                 SessionWizardView):

    template_name = "pricingwizard.html"
    login_url = reverse_lazy('login')

    def done(self, form_list, **kwargs):
        pass
                 
    def get_context_data(self, **kwargs):
        context_data = super(WizardView, self).get_context_data(**kwargs)
        logger.debug("WizardView: get_context_data called with <" + str(kwargs) + "> and context_data <" + str(context_data) + ">")
        context_data['price'] = '0.00'
        progress = (float(context_data['wizard']['steps'].current) + 1) / float(context_data['wizard']['steps'].count) * 100.0
        context_data['progress'] = str(progress) + "%"    
        return context_data

    def get_form_kwargs(self, step):
        logger.debug("WizardView: get_form_kwargs called for step " + str(step))
        return {}
