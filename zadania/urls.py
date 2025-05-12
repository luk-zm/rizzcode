from django.urls import path

from . import views

app_name = "zadania"

urlpatterns = [
    path("", views.index, name="index"),
    # strona glowna zadan
    path("py", views.python, name="python"),
    path("py/<int:zadanie_id>", views.python_zadanie, name="python_zadanie"),
    path("sql", views.sql, name="sql"),


]
