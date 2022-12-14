from django.db import models


class Success_Log(models.Model):
    was_successful = models.BooleanField()
    time_taken = models.DateTimeField()
    reason_for_failure = models.TextField(default="None")


class Train_Data(models.Model):
    train_location = models.IntegerField()
    time_taken = models.DateTimeField()
    train_speed = models.IntegerField()


# train_location
# timestamp
# speed

# sensor
# sensor data