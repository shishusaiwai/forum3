import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from usercenter.models import ActivateCode


def activate(request, code):
    query = ActivateCode.objects.filter(code=code, expire_timestamp__gte=timezone.now())
    if query.count() > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return render(request, "success_hint.html", {"msg": "激活成功", "hint": "去登录", "link": "#"})
    else:
        return render(request, "success_hint.html", {"msg": "激活失败"})


@login_required
def upload_avatar(request):
    if request.method == "GET":
        return render(request, "upload_avatar.html")
    else:
        profile = request.user.userprofile
        avatar_file = request.FILES.get("avatar", None)
        file_path = os.path.join("/usr/share/userres/avatar/", avatar_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in avatar_file.chunks():
                destination.write(chunk)
        url = "http://res.myforum.com/avatar/%s" % avatar_file.name
        profile.avatar = url
        profile.save()
        return redirect("/")
