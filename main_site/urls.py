from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('articles/', views.article_list),
]

