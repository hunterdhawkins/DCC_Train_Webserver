import datetime
import json
import time
from django.shortcuts import render, HttpResponse
from django.db.models.functions import Cast
from django.db.models import IntegerField


def index(request):

    return render(
        request,
        "home/index.html",
        {
        },
    )
