from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CustomerForm
from .models import Customer


class CustomerListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка клиентов.

    Attributes:
        model (Customer): Модель для отображения.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста
        для списка клиентов.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Customer = Customer
    template_name: str = "customers-list.html"
    context_object_name: str = "customers"
    permission_required: str = "customers.view_customer"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на главную страницу.
        """
        return redirect(reverse_lazy("index"))


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о клиенте.

    Attributes:
        model (Customer): Модель для отображения.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста
        для объекта клиента.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Customer = Customer
    template_name: str = "customers-detail.html"
    context_object_name: str = "object"
    permission_required: str = "customers.view_customer"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список клиентов.
        """
        return redirect(reverse_lazy("customers:customer_list"))


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового клиента.

    Attributes:
        model (Customer): Модель для создания.
        form_class (CustomerForm): Форма для создания клиента.
        template_name (str): Имя шаблона для отображения.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления
        после успешного создания.
    """

    model: Customer = Customer
    form_class: CustomerForm = CustomerForm
    template_name: str = "customers-create.html"
    permission_required: str = "customers.add_customer"
    success_url: str = reverse_lazy("customers:customer_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список клиентов.
        """
        return redirect(reverse_lazy("customers:customer_list"))


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего клиента.

    Attributes:
        model (Customer): Модель для редактирования.
        form_class (CustomerForm): Форма для редактирования клиента.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста
        для объекта клиента.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления
        после успешного редактирования.
    """

    model: Customer = Customer
    form_class: CustomerForm = CustomerForm
    template_name: str = "customers-edit.html"
    context_object_name: str = "object"
    permission_required: str = "customers.change_customer"
    success_url: str = reverse_lazy("customers:customer_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список клиентов.
        """
        return redirect(reverse_lazy("customers:customer_list"))


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления клиента.

    Attributes:
        model (Customer): Модель для удаления.
        template_name (str): Имя шаблона для отображения.
        context_object_name (str): Имя переменной контекста
        для объекта клиента.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления
        после успешного удаления.
    """

    model: Customer = Customer
    template_name: str = "customers-delete.html"
    context_object_name: str = "object"
    permission_required: str = "customers.delete_customer"
    success_url: str = reverse_lazy("customers:customer_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список клиентов.
        """
        return redirect(reverse_lazy("customers:customer_list"))
