from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from comments.models import Comment


def comment_ownsership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs["pk"])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        else :
            return func(request, *args, **kwargs)

    return decorated

