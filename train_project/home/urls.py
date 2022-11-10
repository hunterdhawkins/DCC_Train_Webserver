from django.urls import path
from home import html_views, ajax_views


urlpatterns = [
    path("", html_views.feedback, name='home-feedback'),
    path("controls/", html_views.manual_controls, name="home-manual-controls"),
]
