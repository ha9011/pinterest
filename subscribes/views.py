from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

import subscribes
from articles.models import Article
from projects.models import Project
from subscribes.models import Subscribe


@method_decorator(login_required,"get")
@method_decorator(login_required,"post")
class SubscribesView(RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        # 되돌아가기
        return reverse('projects:detail', kwargs={"pk" : self.request.GET.get("project_pk")})

    # get으로 올 경우
    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get("project_pk"))
        user = self.request.user
        subscribe = Subscribe.objects.filter(user=user, project=project)

        if subscribe.exists() :
            subscribe.delete()
        else :
            Subscribe(user=user, project=project).save()
        return super(SubscribesView, self).get(request, *args, **kwargs)
''
@method_decorator(login_required,"get")
class SubscribesListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "subscribes/list.html"
    paginate_by = 5
    
    # 커스텀 마이징 // model에 따라 그냥 긁어 오는데(주어진 값으로 pk면 pk)
    # get_queryset을 하면 내 방식대로 할 수 있음
    def get_queryset(self):
        projects = Subscribe.objects.filter(user =self.request.user).values_list("project")
        article_list = Article.objects.filter(project__in = projects)
        return article_list