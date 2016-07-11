from django.contrib import admin

from .models import ActivateCode, UserProfile


class ActivateCodeAdmin(admin.ModelAdmin):
    list_display = ("owner", "code", "expire_timestamp", "last_update_timestamp")


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "sex", "birthday")
    list_filter = ("sex", )


admin.site.register(ActivateCode, ActivateCodeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
