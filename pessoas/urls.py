from django.urls import path

from produtos import views
from . import views

app_name = 'pessoas'
urlpatterns = [
    # Cliente
    path('listar-clientes/', views.ClienteList.as_view(), name='listar-clientes'),
    path('registrar-cliente/', views.ClienteCreate.as_view(), name='registrar-cliente'),
    path('detalhe-cliente/<int:pk>/', views.ClienteDetail.as_view(), name='detalhe-cliente'),
    path('detalhe-cliente/<int:pk>/excluir/', views.ClienteRemove.as_view(), name='remover-cliente'),
    # Fornecedor
    path('listar-fornecedores/', views.FornecedorList.as_view(), name='listar-fornecedores'),
    path('registrar-fornecedor/', views.FornecedorCreate.as_view(), name='registrar-fornecedor'),
    path('detalhe-fornecedor/<int:pk>/', views.FornecedorDetail.as_view(), name='detalhe-fornecedor'),
    path('detalhe-fornecedor/<int:pk>/excluir/', views.FornecedorRemove.as_view(), name='remover-fornecedor'),
    ]