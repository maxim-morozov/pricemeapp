from django.contrib import admin
from .submodels.userprofile import UserProfile

# Register your models here.
admin.site.register(UserProfile)
