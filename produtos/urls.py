from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns = [
    path('', views.ProdutosList.as_view(), name='listar'),
    path('registrar/', views.ProdutosCreate.as_view(), name='registrar'),
    path('detalhes/<int:pk>/', views.ProdutoDetail.as_view(), name='detalhes'),
    path('detalhes/<int:pk>/excluir/', views.ProdutoRemove.as_view(), name='excluir'),
]