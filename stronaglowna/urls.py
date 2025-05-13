from django.urls import path

from . import views

app_name = "stronaglowna"

urlpatterns = [
    path("", views.index, name="index"),
]
