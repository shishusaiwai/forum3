import json

from django.http import HttpResponse


def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)
