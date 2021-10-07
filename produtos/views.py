from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from pessoas import models

from .forms import RegistroCategoriaForm, RegistroMarcaForm, RegistroProdutosForm

from produtos.models import Categoria, Marca, Produto

# CATEGORIA
class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    paginate_by = 50


class CategoriaCreate(LoginRequiredMixin, CreateView):
    template_name = 'produtos/categoria_form.html'
    model = Categoria
    form_class = RegistroCategoriaForm
    success_url = reverse_lazy('produtos:categoria-listar')


class CategoriaDetail(LoginRequiredMixin, UpdateView):
    template_name = 'produtos/categoria_detail.html'
    model = Categoria
    form_class = RegistroCategoriaForm
    success_url = reverse_lazy('produtos:categoria-listar')


class CategoriaRemove(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('produtos:categoria-listar')


# MARCA
class MarcaList(LoginRequiredMixin, ListView):
    model = Marca
    paginate_by = 50


class MarcaCreate(LoginRequiredMixin, CreateView):
    template_name = 'produtos/marca_form.html'
    model = Marca
    form_class = RegistroMarcaForm
    success_url = reverse_lazy('produtos:marca-listar')


class MarcaDetail(LoginRequiredMixin, UpdateView):
    template_name = 'produtos/marca_detail.html'
    model = Marca
    form_class = RegistroMarcaForm
    success_url = reverse_lazy('produtos:marca-listar')


class MarcaRemove(LoginRequiredMixin, DeleteView):
    model = Marca
    success_url = reverse_lazy('produtos:marca-listar')


# PRODUTO
class ProdutosList(LoginRequiredMixin, ListView):
    model = Produto
    paginate_by = 50


class ProdutosCreate(LoginRequiredMixin, CreateView):
    template_name = 'produtos/produto_form.html'
    model = Produto
    form_class = RegistroProdutosForm
    success_url = reverse_lazy('produtos:listar')


class ProdutoDetail(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'produtos/produto_detail.html'
    form_class = RegistroProdutosForm
    success_url = reverse_lazy('produtos:listar')


class ProdutoRemove(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('produtos:listar')
