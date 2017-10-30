from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from django.conf import settings
from authapp.subforms import passwordmanagementforms as forms
import logging

User = get_user_model()
logger = logging.getLogger(settings.PROJECT_LOGGER)

class PasswordChangeView(authviews.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'password-change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request,
                         "Your password was changed, "
                         "hence you have been logged out. Please relogin")
        return super(PasswordChangeView, self).form_valid(form)


class PasswordResetView(authviews.PasswordResetView):
    form_class = forms.PasswordResetForm
    template_name = 'password-reset.html'
    success_url = reverse_lazy('password-reset-done')
    subject_template_name = 'emails/password-reset-subject.txt'
    email_template_name = 'emails/password-reset-email.html'


class PasswordResetDoneView(authviews.PasswordResetDoneView):
     template_name = 'password-reset-done.html'


class PasswordResetConfirmView(authviews.PasswordResetConfirmAndLoginView):
    template_name = 'password-reset-confirm.html'
    form_class = forms.SetPasswordForm
    success_url = reverse_lazy('home')
