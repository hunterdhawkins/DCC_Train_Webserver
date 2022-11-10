from django.urls import path
from home import html_views, ajax_views


urlpatterns = [
    path("", html_views.feedback, name='home-feedback'),
    # path("steps/", views.required_steps, name="home-required-steps"),
]
