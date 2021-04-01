from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articles.models import Article
from comments.decorators import comment_ownsership_required
from comments.forms import CommentsCreationForm
from comments.models import Comment


class CommentsCreateView(CreateView):
    model = Comment
    form_class = CommentsCreationForm
    template_name = "comments/create.html"

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST["article_pk"])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articles:detail", kwargs={"pk": self.object.article.pk})

@method_decorator(comment_ownsership_required,"get")
@method_decorator(comment_ownsership_required,"post")
class CommentsDeleteView(DeleteView):
    model = Comment
    context_object_name = "target_comment"
    template_name = "comments/delete.html"


    def get_success_url(self):
        return reverse("articles:detail", kwargs={"pk": self.object.article.pk})


## 업데이트 혼자 해보기

