from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user # 작성자가 누군지 연결
        form.instance.article_id = self.request.POST.get('article_pk') # 게시글이 뭔지 연결. 템플릿에서 추가적인 정보 넘겨줘야 함
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
