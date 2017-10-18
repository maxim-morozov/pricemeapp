from django.core.urlresolvers import reverse_lazy
from authtools import views as authviews

class LogoutView(authviews.LogoutView):
    url = reverse_lazy('home')
