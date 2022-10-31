from django.db import models


class Success_Log(models.Model):
    was_successful = models.BooleanField()
    time_taken = models.DateTimeField()
    reason_for_failure = models.TextField(default="None")
