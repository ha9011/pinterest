from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profiles.models import Profile


def profile_ownsership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs["pk"])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        else :
            return func(request, *args, **kwargs)

    return decorated

