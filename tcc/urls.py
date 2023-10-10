from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/proposta/', views.cadastro_proposta),
]
