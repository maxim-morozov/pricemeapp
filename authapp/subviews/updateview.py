from django.conf import settings
import logging
from django.contrib.auth import get_user_model
from braces import views as bracesviews
from django.views import generic
from authapp.subforms.userform import UserForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class UpdateView(bracesviews.LoginRequiredMixin,
                 bracesviews.FormValidMessageMixin,
                 generic.UpdateView):
    
    form_class = UserForm
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You've updated your profile!"
    login_url = 'login.html'

    def get_object(self, queryset=None):
        logger.debug("Get object called")
        return self.request.user
    
    def get_form_kwargs(self, **kwargs):
        logger.debug("Get form kwargs get called")
        form_kwargs = super(UpdateView, self).get_form_kwargs(**kwargs)
        form_kwargs["instance"] = self.request.user
        return form_kwargs    

    def get_success_url(self):
        logger.debug("Get success url get called and returned " + reverse('home'))
        return reverse('home')

    def form_valid(self, form):
        user = super(UpdateView, self).form_valid(form)
        logger.debug("Updated the form for: " + str(user))
        return user

    def form_invalid(self, form):
        response = super(UpdateView, self).form_invalid(form)
        logger.debug("Form invalid with response: " + str(form.errors))
        return response
    
                 

