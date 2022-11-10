import json
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from home import utils


"""
    AJAX Views
"""


@csrf_exempt
def read_some_data(request):
    pass
    # tag_name = request.POST.get("tag_name", None)
    # if tag_name is None:
    #     return JsonResponse({"result": "failed", "message": "Missing Tag Name"})

    # data = utils.read_tag([tag_name])

    # return JsonResponse({"result": "success", "data": json.dumps(data[0])})
