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

    # Get information from the train
    feedback_dict = utils.read_train_status()
    train_speed = feedback_dict['speed']
    train_headlight = feedback_dict['headlight']
    train_direction = feedback_dict['direction']

    # User wants to change info about the train
    if request.method == 'POST':
        train_speed_input = request.POST.get("speed")
        train_headlight_input = request.POST.get("toggle_headlight")
        train_direction_input = request.POST.get("direction")
        if train_headlight_input is None:
            train_headlight_input = False
        utils.write_data_to_train(train_speed_input, train_headlight_input, train_direction_input)

    return render(
        request,
        "home/controls.html",
        {
            'speed': train_speed,
            'headlight': train_headlight,
            'direction': train_direction,
        },

    )
