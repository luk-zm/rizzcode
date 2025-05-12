from django.urls import path
from . import views

app_name = "zadania"

urlpatterns = [
    path('zadania/', views.zadania, name='zadania'),
    # strona glowna zadan

]

