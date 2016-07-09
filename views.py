import datetime
import uuid

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from usercenter.models import ActivateCode
from block.models import Block
from message.models import UserMessage


def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    if request.user.is_authenticated():
        msg_cnt = UserMessage.objects.filter(status=0, owner=request.user).count()
    else:
        msg_cnt = 0
    return render(request, "index.html", {"blocks": block_infos, "msg_cnt": msg_cnt})


def register(request):
    error = ""
    if request.method == "GET":
        return render(request, "register.html", {})
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()
        if not username or not password or not email:
            error = "任何字段都不能为空"
        if password != re_password:
            error = "两次密码不一致"
        if User.objects.filter(username=username).count() > 0:
            error = "用户已存在"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            new_code = str(uuid.uuid4()).replace("-", "")
            expire_time = timezone.now() + datetime.timedelta(days=2)
            code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
            code_record.save()

            activate_link = "http://%s/activate/%s" % (request.get_host(), new_code)
            activate_email = '''点击<a href="%s">这里</a>激活''' % activate_link
            send_mail(subject='[Python部落论坛]激活邮件',
                      message='点击链接激活: %s' % activate_link,
                      html_message=activate_email,
                      from_email='564630776@qq.com',
                      recipient_list=[email],
                      fail_silently=False)
        else:
            return render(request, "register.html", {"error": error})
        return render(request, "success_hint.html", {"msg": "注册成功，激活邮件已经发送到您的邮箱，请点击邮箱中的激活链接完成激活。"})
