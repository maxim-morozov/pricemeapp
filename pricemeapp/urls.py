"""pricemeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from authapp.subviews.registerview import RegisterView
from authapp.subviews.logoutview import LogoutView
from authapp.subviews.loginview import LoginView
from authapp.subviews.updateview import UpdateView
from authapp.subviews.passwordmanagementviews import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^profile/$', UpdateView.as_view(), name='profile'),
    url(r'^change-password/$', PasswordChangeView.as_view(), name='password-change'),
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password-reset'),
    url(r'^password-reset-done/$', PasswordResetDoneView.as_view(), name='password-reset-done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$$', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    
]
