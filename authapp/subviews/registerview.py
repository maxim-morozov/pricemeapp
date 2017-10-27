from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from authapp.subforms.userform import UserForm
from extra_views import CreateWithInlinesView, InlineFormSet
from authapp.submodels.userprofile import UserProfile
import logging
from django.conf import settings

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class RegisterView(bracesviews.AnonymousRequiredMixin,
                   bracesviews.FormValidMessageMixin,
                   generic.CreateView):
    form_class = UserForm
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You're signed up!"
    
    def form_valid(self, form):
        r = super(RegisterView, self).form_valid(form)
        
        username = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        logger.debug("Saved user successfully: " + str(username) + " " + str(password))
        user = auth.authenticate(email=username, password=password)
        logger.debug("Saved user successfully: " + str(user))
        
        auth.login(self.request, user)
        return r


            
            
