from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "title", "status", "create_timestamp", "last_update_timestamp")


admin.site.register(Article, ArticleAdmin)
