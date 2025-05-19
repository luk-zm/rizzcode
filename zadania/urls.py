from django.urls import path
from . import views

urlpatterns = [
    path('', views.zadania, name='exercise-list'),
    path('submit/<int:exercise_id>/', views.submit_solution, name='submit-solution'),
    path('szczegoly/<int:exercise_id>/', views.szczegoly_zadania, name='exercise-detail'),
    path('<str:lang>/', views.zadania_po_jezyku, name='exercise-by-language'),
    path('upload/<int:exercise_id>/', views.upload_solution, name='upload-solution'),
    path('submit_sql/<int:exercise_id>/', views.submit_sql_solution, name='submit-sql-solution'),
]
