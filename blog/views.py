from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category

# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article_detail'
    template_name = 'detail.html'
    pk_url_kwarg = 'article_id'

    # def get_object(self, queryset=None):
    #     obj = super(ArticleDetailView, self).get_object()
    #     return obj

    def get(self, request, article_id):
        article_detail = Article.objects.get(id=int(article_id))
        return render(request, "article_detail.html", {"article_detail": article_detail})


