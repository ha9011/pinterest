from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articles.models import Article
from projects.models import Project


def project_ownsership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs["pk"])
        if not project.writer == request.user:
            return HttpResponseForbidden()
        else :
            return func(request, *args, **kwargs)

    return decorated

