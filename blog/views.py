from django.shortcuts import render
from .models import Article, Category, Tag
from django.views.generic import ListView, DetailView

# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     context['category'] = Category.objects.all()
    #     return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article_detail'
    template_name = 'detail.html'
    pk_url_kwarg = 'article_id'

