from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profiles.forms import ProfileCreationForm
from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name =  "target_profile"
    form_class = ProfileCreationForm
    success_url = reverse_lazy("account:hello_world")
    template_name = "profiles/create.html"


    # 인자 값이 있는 form은  클라이언트에서 온 데이터가 -> form_class = ProfileCreationForm 여기로 이동 되어
    # form obj에 담겨조 옴
    def form_valid(self, form):
        temp_profile = form.save(commit=False) # 저장이 아닌 단순 격납이기에 commit False
        temp_profile.user = self.request.user # form엔 유저가 없어서 격납 가능(model에는 있으니깐 user가..)
        temp_profile.age = 20
        temp_profile.save()
        return super().form_valid(form)
        # 이 리턴된 값으로 view가 이용하여 Db에 저장