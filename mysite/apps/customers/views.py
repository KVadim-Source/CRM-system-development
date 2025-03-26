from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm


class CustomerListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка клиентов.

    Attributes:
        model (Customer): Модель для отображения.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста для списка клиентов.
        permission_required (str): Необходимое разрешение для доступа к представлению.
    """
    model: Customer = Customer
    template_name: str = 'customers-list.html'
    context_object_name: str = 'customers'
    permission_required: str = 'customers.can_view_customer'


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о клиенте.

    Attributes:
        model (Customer): Модель для отображения.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста для объекта клиента.
        permission_required (str): Необходимое разрешение для доступа к представлению.
    """
    model: Customer = Customer
    template_name: str = 'customers-detail.html'
    context_object_name: str = 'object'
    permission_required: str = 'customers.can_view_customer'


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового клиента.

    Attributes:
        model (Customer): Модель для создания.
        form_class (CustomerForm): Форма для создания клиента.
        template_name (str): Имя шаблона для отображения.
        permission_required (str): Необходимое разрешение для доступа к представлению.
        success_url (str): URL для перенаправления после успешного создания.
    """
    model: Customer = Customer
    form_class: CustomerForm = CustomerForm
    template_name: str = 'customers-create.html'
    permission_required: str = 'customers.can_add_customer'
    success_url: str = reverse_lazy('customers:customer_list')


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего клиента.

    Attributes:
        model (Customer): Модель для редактирования.
        form_class (CustomerForm): Форма для редактирования клиента.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста для объекта клиента.
        permission_required (str): Необходимое разрешение для доступа к представлению.
        success_url (str): URL для перенаправления после успешного редактирования.
    """
    model: Customer = Customer
    form_class: CustomerForm = CustomerForm
    template_name: str = 'customers-edit.html'
    context_object_name: str = 'object'
    permission_required: str = 'customers.can_change_customer'
    success_url: str = reverse_lazy('customers:customer_list')


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления клиента.

    Attributes:
        model (Customer): Модель для удаления.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста для объекта клиента.
        permission_required (str): Необходимое разрешение для доступа к представлению.
        success_url (str): URL для перенаправления после успешного удаления.
    """
    model: Customer = Customer
    template_name: str = 'customers-delete.html'
    context_object_name: str = 'object'
    permission_required: str = 'customers.can_delete_customer'
    success_url: str = reverse_lazy('customers:customer_list')
