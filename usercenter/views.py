from django.utils import timezone
from django.shortcuts import render
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
