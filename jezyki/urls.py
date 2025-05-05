from django.urls import path
from . import views

urlpatterns = [
    path('jezyki/', views.jezyki, name='jezyki')
]