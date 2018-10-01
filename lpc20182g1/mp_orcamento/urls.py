from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),    
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('orcamentos/cliente/<int:codigo>', orc_cliente, name='orc_cliente'),
    path('orcamentos/cliente/estatisticas', cliente_estatisticas, name='cliente_estatisticas')
    
]
