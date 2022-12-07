import datetime
import json
import time
from django.shortcuts import render, HttpResponse
from django.db.models.functions import Cast
from django.db.models import IntegerField
from home import utils


def feedback(request):

    return render(
        request,
        "home/feedback.html",
        {
        },
    )


def fake_factory(request):
    num_of_red = None
    num_of_white = None
    num_of_blue = None
    num_of_faulty = None
    if request.method == 'POST':
        num_of_red = request.POST.get("num_of_red")
        num_of_white = request.POST.get("num_of_white")
        num_of_blue = request.POST.get("num_of_blue")
        num_of_faulty = request.POST.get("num_of_faulty")

    print("*******************")
    print(num_of_red, num_of_white, num_of_blue, num_of_faulty)
    print("*******************")

    return render(
        request,
        "home/fake_factory.html",
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

        print("train speed" + train_speed_input)
        # Default to existing headlight
        if train_headlight_input is None:
            train_headlight_input = train_headlight
        # Default to the existing speed
        if train_speed_input is None:
            train_speed_input = train_speed
        if train_direction_input is None:
            train_direction_input = train_direction

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
