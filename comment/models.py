from django.contrib.auth.models import User
from django.db import models

from article.models import Article


class DeletedCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=-1)


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=0)


class Comment(models.Model):
    objects = models.Manager()
    normal_objects = CommentManager()
    deleted_objects = DeletedCommentManager()

    owner = models.ForeignKey(User, verbose_name="作者")
    article = models.ForeignKey(Article, verbose_name="所属文章")
    content = models.CharField(u"内容", max_length=10000, blank=True)
    status = models.IntegerField(u"状态", choices=((0, u"普通"), (-1, u"删除")), default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
