from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('watch/', views.watch, name='watch'),
    path('feedback/', views.feedback, name='feedback'),
]
