from django.urls import path
from . import views

urlpatterns = [
    path('E_commerce/', views.E_commerce, name='E_commerce'),
]
