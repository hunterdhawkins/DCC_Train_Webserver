from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name='home-index'),
    # path("steps/", views.required_steps, name="home-required-steps"),
]
