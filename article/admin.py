from django.contrib import admin

from comment.models import Comment
from .models import Article


class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False
    extra = 4


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "title", "status", "create_timestamp", "last_update_timestamp")
    actions = ["make_picked"]
    inlines = [CommentInline]
    fieldsets = (
        ("基本", {"classes": ("",), "fields": ("title", "content")}),
        ("高级", {"classes": ('collapse',), "fields": ("status", )})
    )

    def make_picked(modeladmin, request, queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = "设置精华"


admin.site.register(Article, ArticleAdmin)
