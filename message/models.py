from django.db import models
from django.contrib.auth.models import User


class UserMessage(models.Model):
    owner = models.ForeignKey(User, verbose_name="作者")
    content = models.CharField("内容", max_length=400)
    link = models.CharField("链接", max_length=400)
    status = models.IntegerField("状态", choices=((0, "未读"), (1, "已读")), default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = "用户消息"
