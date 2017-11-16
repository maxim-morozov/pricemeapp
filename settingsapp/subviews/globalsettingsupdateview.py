from django.conf import settings
import logging
from django.contrib.auth import get_user_model
from braces import views as bracesviews
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from settingsapp.submodels.globalsettingsmodel import GlobalSettings
from settingsapp.subforms.globalsettingsform import GlobalSettingsForm
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class GlobalSettingsUpdateView(bracesviews.LoginRequiredMixin,
                               bracesviews.FormValidMessageMixin,
                               generic.UpdateView):
    model = GlobalSettings
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    form_valid_message = "You've updated your settings!"
    form_class = GlobalSettingsForm
    template_name = "globalsettings.html"

    def get_queryset(self):
        queryset = super(GlobalSettingsUpdateView, self).get_queryset()
        logger.debug("GlobalSettings recieved the queryset: " + str(queryset))
        fileteredQuerySet = queryset.filter(user=self.request.user)
        logger.debug("GlobalSettings recieved filtered queryset: " + str(fileteredQuerySet))
        return fileteredQuerySet

    def get_object(self, queryset=None):
        logger.debug("GlobalSettings retrieving the object with the queryset: " + str(queryset))

        # First we should get the queryset
        if queryset is None:
            queryset = self.get_queryset()
            logger.debug("GlobalSettings updating the queryset: " + str(queryset))

        # Retrieve the object from the query set
        try:
            obj = queryset.get()
            logger.debug("GlobalSettings object retrieved: " + str(obj))
        except ObjectDoesNotExist:
            # We don't have the settings yet saved for this user
            logger.debug("GlobalSettings current user doesn't have settings yet saved")
            # We will create new settings for this user
            obj = GlobalSettings.objects.create_or_update(user=self.request.user)

        # Return the retrieved or newly initialised object    
        return obj

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(GlobalSettingsUpdateView, self).get_form_kwargs(**kwargs)
        form_kwargs["instance"] = self.object
        return form_kwargs


    def form_valid(self, form):
        globalsettings = super(GlobalSettingsUpdateView, self).form_valid(form)
        logger.debug("Updated the form for: " + str(globalsettings))
        return globalsettings

    def form_invalid(self, form):
        response = super(GlobalSettingsUpdateView, self).form_invalid(form)
        logger.debug("Form invalid with response: " + str(form.errors))
        return response
        
    
