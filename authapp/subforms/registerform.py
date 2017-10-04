from django import forms
from authapp.models.submodels import User

class RegisterForm(forms.ModelForm):
    
    class Meta:
        # Provide association with the User object
        model = User

        # Populate the fields required in the form
        fields = ('first_name', 'last_name', 'company_name', 'web_address', 'email', 'password')
