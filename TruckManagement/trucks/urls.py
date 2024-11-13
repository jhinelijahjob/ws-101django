from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('trucks/', views.trucks, name='trucks'),
    path('trucks/info/<int:engine_model>', views.info, name='info'),
    path('testing/', views.testing, name='testing'),
]
