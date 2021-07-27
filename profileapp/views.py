from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')    # 우선 hello_world 페이지로
    template_name = 'profileapp/create.html'    # 추후에 만들 html 파일

    def form_valid(self, form):  # 검증이 완료되면 form_valid 함수가 적용된다. 커스터마이징 하려고 오버라이딩
        form.instance.user = self.request.user  # user를 할당한 것!(forms.py에는 user가 필드에 없으므로)
        return super().form_valid(form)