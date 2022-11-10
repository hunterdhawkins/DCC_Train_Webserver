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
    feedback_dict = utils.read_train_status()
    train_speed = feedback_dict['speed']
    train_headlight = feedback_dict['headlight']
    return render(
        request,
        "home/controls.html",
        {
            'speed': train_speed,
            'headlight': train_headlight,
        },

    )
