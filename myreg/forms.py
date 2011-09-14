from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationForm, RegistrationFormTermsOfService, RegistrationFormUniqueEmail


class AuthAndUnActiveForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
 
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))
        self.check_for_test_cookie()
        return self.cleaned_data
        
        
class TermsAndUniqueRegForm(RegistrationFormTermsOfService):
    
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']