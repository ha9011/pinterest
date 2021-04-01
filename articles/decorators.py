from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articles.models import Article


def article_ownsership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs["pk"])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        else :
            return func(request, *args, **kwargs)

    return decorated

