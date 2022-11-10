import datetime
import json
import time
from django.shortcuts import render, HttpResponse
from django.db.models.functions import Cast
from django.db.models import IntegerField
from home import utils


def feedback(request):
    utils.modbus_quick_check()
    return render(
        request,
        "home/feedback.html",
        {
        },
    )


def manual_controls(request):
    return render(
        request,
        "home/controls.html",
        {

        },

    )
