from django.urls import path
from . import views

urlpatterns = [
    path('', views.zadania, name='exercise-list'),
    path('<str:lang>/', views.zadania_po_jezyku, name='exercise-by-language'),
    path('szczegoly/<int:exercise_id>/', views.szczegoly_zadania, name='exercise-detail'),
]
