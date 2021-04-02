from django.forms import ModelForm
from django import forms
from articles.models import Article
from projects.models import Project


class ArticleCreationForm(ModelForm):

    # html form 형태를 커스텀 마이징
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"editable ",

                                                           "style":"height:auto text-align:left"}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    # 내가 만든 프로젝트에서만 글 올릴수있게 하기

    class Meta :
        model = Article
        fields = ["title", "image", "project", "content"]
