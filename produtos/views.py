from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RegistroProdutosForm

from produtos.models import Produto

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
