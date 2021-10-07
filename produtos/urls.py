from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns = [
    path('', views.ProdutosList.as_view(), name='listar'),
    path('registrar/', views.ProdutosCreate.as_view(), name='registrar'),
    path('detalhes/<int:pk>/', views.ProdutoDetail.as_view(), name='detalhes'),
    path('detalhes/<int:pk>/excluir/', views.ProdutoRemove.as_view(), name='excluir'),
    #categoria
    path('categoria/', views.CategoriaList.as_view(), name='categoria-listar'),
    path('categoria-registrar/', views.CategoriaCreate.as_view(), name='categoria-registrar'),
    path('categoria-detalhes/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detalhes'),
    path('categoria-detalhes/<int:pk>/excluir/', views.CategoriaRemove.as_view(), name='categoria-remover'),
    #marca
    path('marca/', views.MarcaList.as_view(), name='marca-listar'),
    path('marca-registrar/', views.MarcaCreate.as_view(), name='marca-registrar'),
    path('marca-detalhes/<int:pk>/', views.MarcaDetail.as_view(), name='marca-detalhes'),
    path('marca-detalhes/<int:pk>/excluir/', views.MarcaRemove.as_view(), name='marca-remover'),
]