from django.shortcuts import render
from .models import Post
from django.views.generic import View, DetailView

# Create your views here.

class MainPageView(View):

    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        return render(request, 'main_page.html', context={'posts': posts})


class NewsDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news_detail.html'