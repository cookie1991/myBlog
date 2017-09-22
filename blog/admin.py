from django.contrib import admin
from .models import Article, Category, Tag, Project

# Register your models here.


admin.site.register([Article, Category, Tag, Project])

