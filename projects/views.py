from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article
from projects.forms import ProjectCreationForm
from projects.models import Project
from subscribes.models import Subscribe


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projects/create.html"

    def get_success_url(self):
        print("...")
        return reverse("projects:detail", kwargs={"pk" : self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin): # 여러가지 믹스인을 다를 수 있음
    model = Project
    context_object_name = "target_project"
    template_name = "projects/detail.html"

    #추가
    paginate_by = 25

    def get_context_data(self, **kwargs):

        project = self.object
        user = self.request.user
        subscribe = None
        if user.is_authenticated :
            subscribe = Subscribe.objects.filter(user=user, project=project)

        object_list = Article.objects.filter(project=self.get_object())
        # self.get_object() : 현재 클레스의 오브젝트 ( project )
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscribe=subscribe, **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "projects/list.html"
    paginate_by = 25
