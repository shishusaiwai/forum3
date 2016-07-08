from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("owner", "article", "content", "status", "last_update_timestamp")
    list_filter = ("status", )


admin.site.register(Comment, CommentAdmin)
