from django.core.urlresolvers import reverse_lazy
from authtools import views as authviews
from django.conf import settings
from braces import views as bracesviews
from django.contrib.auth import get_user_model
from django.views import generic
from authapp.subforms.loginform import LoginForm
from django.contrib import auth

User = get_user_model()

class LoginView(bracesviews.AnonymousRequiredMixin,
                authviews.LoginView):
    
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    form_class = LoginForm

    def form_valid(self, form):
        redirect = super(LoginView, self).form_valid(form)
        remember_me = form.cleaned_data.get('remember_me')
        
        if remember_me is True:
            ONE_MONTH = 30*24*60*60
            expiry = getattr(settings, "KEEP_LOGGED_DURATION", ONE_MONTH)
            self.request.session.set_expiry(expiry)

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = auth.authenticate(email=username, password=password)
        auth.login(self.request, user)
        return redirect
