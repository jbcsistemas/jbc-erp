from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic.list import ListView

from .forms import RegistroClienteForm, RegistroFornecedorForm
from .models import Cliente, Fornecedor

# CLIENTE
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    paginate_by = 50


class ClienteCreate(LoginRequiredMixin, CreateView):
    template_name = 'pessoas/cliente_form.html'
    model = Cliente
    form_class = RegistroClienteForm
    success_url = reverse_lazy('pessoas:listar-clientes')


class ClienteDetail(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'pessoas/cliente_detail.html'
    form_class = RegistroClienteForm
    success_url = reverse_lazy('pessoas:listar-clientes')


class ClienteRemove(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('pessoas:listar-clientes')


# FORNECEDOR
class FornecedorList(LoginRequiredMixin, ListView):
    model = Fornecedor
    paginate_by = 50


class FornecedorCreate(LoginRequiredMixin, CreateView):
    template_name = 'pessoas/fornecedor_form.html'
    model = Fornecedor
    form_class = RegistroFornecedorForm
    success_url = reverse_lazy('pessoas:listar-fornecedores')


class FornecedorDetail(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    template_name = 'pessoas/fornecedor_detail.html'
    form_class = RegistroFornecedorForm
    success_url = reverse_lazy('pessoas:listar-fornecedores')


class FornecedorRemove(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('pessoas:listar-fornecedores')
