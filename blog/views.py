from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category, Tag, Project

# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['project_list'] = Project.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'detail.html'
    pk_url_kwarg = 'article_id'


class CategoryView(ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        return article_list


class ProjectView(ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(project=self.kwargs['project_id'], status='p')
        return article_list


