from django.db import models

# Create your models here.


class Article(models.Model):

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')

    # 创建时间，不可被覆盖
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text='可选项，若为空格则摘取正文前54个字符')

    views = models.PositiveIntegerField('浏览量', default=0)

    likes = models.PositiveIntegerField('点赞数', default=0)

    topped = models.BooleanField('置顶', default=False)

    tag = models.ManyToManyField('Tag', verbose_name='标签')

    category = models.ForeignKey('Category', verbose_name='分类', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']


class Category(models.Model):

    name = models.CharField('分类', max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField('标签', max_length=20)

    def __str__(self):
        return self.name



