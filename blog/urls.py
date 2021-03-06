"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import ArticleListView, ArticleDetailView, CategoryView, ProjectView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r"^category/(?P<cate_id>\d+)$", CategoryView.as_view(), name='category'),
    url(r"^project/(?P<project_id>\d+)$", ProjectView.as_view(), name='project')
]
