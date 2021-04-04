from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articles.models import Article
from likes.models import Like


@method_decorator(login_required,"get")
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("articles:detail", kwargs={"pk" : kwargs["pk"] })

    def get(self, request, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs["pk"])

        if Like.objects.filter(user=user, article=article).exists():
            messages.add_message(self.request, messages.ERROR, "좋아요는 한번만 가능합니다.")
            return HttpResponseRedirect(reverse("articles:detail", kwargs={"pk" : kwargs["pk"] }))
        else :

            Like(user=user, article=article).save()

        article.like += 1
        article.save()

        messages.add_message(self.request, messages.SUCCESS, "좋아요가 반영되었습니다.")

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)