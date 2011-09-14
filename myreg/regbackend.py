from django.contrib.sites.models import Site

from registration.backends.default import DefaultBackend
from registration import signals
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile
from people.models import Person


class PersonBackend(DefaultBackend):
    def activate(self, request, activation_key):
        """
        Given an an activation key, look up and activate the user
        account corresponding to that key (if possible).

        After successful activation, the signal
        ``registration.signals.user_activated`` will be sent, with the
        newly activated ``User`` as the keyword argument ``user`` and
        the class of this backend as the sender.
        
        """
        activated = RegistrationProfile.objects.activate_user(activation_key)
        if activated:
            signals.user_activated.send(sender=self.__class__,
                                        user=activated,
                                        request=request)
            person = Person(user=activated)
            activated.save()
            person.save()
        return activated