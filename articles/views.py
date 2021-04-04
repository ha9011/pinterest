from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articles.decorators import article_ownsership_required
from articles.forms import ArticleCreationForm
from articles.models import Article
from comments.forms import CommentsCreationForm


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articles/create.html"

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articles:detail", kwargs={"pk" : self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentsCreationForm
    template_name = "articles/detail.html"
    context_object_name = "target_article"




@method_decorator(article_ownsership_required,"get")
@method_decorator(article_ownsership_required,"post")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = "target_article"
    template_name = "articles/update.html"



    def get_success_url(self):
        return reverse("articles:detail", kwargs={"pk": self.object.pk})


@method_decorator(article_ownsership_required,"get")
@method_decorator(article_ownsership_required,"post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "target_article"
    template_name = "articles/delete.html"


    def get_success_url(self):
        return reverse("articles:list")


class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "articles/list.html"
    paginate_by = 25  # 보여질 obj 갯수

