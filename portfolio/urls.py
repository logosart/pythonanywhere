from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ="home"),
     path('materias/', views.materias, name='materias')
]
