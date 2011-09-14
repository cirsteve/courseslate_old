from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from registration.views import register, activate
from django.contrib.auth.views import login

from myreg.forms import TermsAndUniqueRegForm

urlpatterns = patterns('',
    url(r'^activate/(?P<activation_key>\w+)/$', activate,
        {'backend': 'myreg.regbackend.PersonBackend',
        'success_url': '/people/'},
        name='registration_activate'),
    url(r'^register/$', register,
        {'backend': 'registration.backends.default.DefaultBackend',
        'form_class': TermsAndUniqueRegForm,
        'template_name': 'myreg/tosregistration_form.html',
        'success_url': '/'},
        name='registration_register'),
        )