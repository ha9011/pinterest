from django.forms import ModelForm

from comments.models import Comment


class CommentsCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]