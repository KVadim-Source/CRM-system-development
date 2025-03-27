import os
from typing import Optional

from django.conf import settings
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

from .forms import ContractForm
from .models import Contract


def checking_file(file) -> Optional[str]:
    """
    Проверяет наличие файла и возвращает уникальное имя файла.

    Args:
        file: Загружаемый файл.

    Returns:
        Optional[str]: Уникальное имя файла или None.
    """
    if file:
        file_name, file_extension = os.path.splitext(file.name)
        media_path = os.path.join(settings.MEDIA_ROOT, file.name)

        if not os.path.exists(media_path):
            return file.name

        counter = 1
        while True:
            new_name = f"{file_name}_{counter}{file_extension}"
            media_path = os.path.join(settings.MEDIA_ROOT, new_name)
            if not os.path.exists(media_path):
                return new_name
            counter += 1
    return None


class ContractListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка контрактов.

    Attributes:
        model (Contract): Модель контракта.
        template_name (str): Шаблон для отображения списка.
        context_object_name (str): Имя контекста для списка контрактов.
        permission_required (str): Разрешение для просмотра контрактов.
    """

    model: Contract = Contract
    template_name: str = "contracts-list.html"
    context_object_name: str = "contracts"
    permission_required: str = "contracts.view_contract"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на главную страницу.
        """
        return redirect(reverse_lazy('index'))


class ContractDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения деталей контракта.

    Attributes:
        model (Contract): Модель контракта.
        template_name (str): Шаблон для отображения деталей.
        context_object_name (str): Имя контекста для контракта.
        permission_required (str): Разрешение для просмотра контракта.
    """

    model: Contract = Contract
    template_name: str = "contracts-detail.html"
    context_object_name: str = "contract"
    permission_required: str = "contracts.view_contract"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список контрактов.
        """
        return redirect(reverse_lazy("contract:contract_list"))


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового контракта.

    Attributes:
        model (Contract): Модель контракта.
        form_class (ContractForm): Форма для создания контракта.
        template_name (str): Шаблон для создания контракта.
        permission_required (str): Разрешение для добавления контракта.
    """

    model: Contract = Contract
    form_class: ContractForm = ContractForm
    template_name: str = "contracts-create.html"
    permission_required: str = "contracts.add_contract"

    def form_valid(self, form) -> None:
        """
        Обработка формы при создании контракта.

        Args:
            form: Форма контракта.

        Returns:
            None
        """
        uploaded_file = self.request.FILES.get("document")
        if uploaded_file:
            uploaded_file.name = checking_file(uploaded_file)
        return super().form_valid(form)

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список контрактов.
        """
        return redirect(reverse_lazy("contract:contract_list"))


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования контракта.

    Attributes:
        model (Contract): Модель контракта.
        form_class (ContractForm): Форма для редактирования контракта.
        template_name (str): Шаблон для редактирования контракта.
        permission_required (str): Разрешение для изменения контракта.
    """

    model: Contract = Contract
    form_class: ContractForm = ContractForm
    template_name: str = "contracts-edit.html"
    permission_required: str = "contracts.change_contract"

    def form_valid(self, form) -> None:
        """
        Обработка формы при редактировании контракта.

        Args:
            form: Форма контракта.

        Returns:
            None
        """
        uploaded_file = self.request.FILES.get("document")
        if uploaded_file:
            uploaded_file.name = checking_file(uploaded_file)
        return super().form_valid(form)

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список контрактов.
        """
        return redirect(reverse_lazy("contract:contract_list"))


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления контракта.

    Attributes:
        model (Contract): Модель контракта.
        template_name (str): Шаблон для подтверждения удаления.
        success_url (str): URL для перенаправления после удаления.
        permission_required (str): Разрешение для удаления контракта.
    """

    model: Contract = Contract
    template_name: str = "contracts-delete.html"
    success_url: str = "/contracts/"
    permission_required: str = "contracts.delete_contract"

    def delete(self, request, *args, **kwargs) -> None:
        """
        Обработка удаления контракта.

        Args:
            request: Запрос.
            *args: Дополнительные аргументы.
            **kwargs: Именованные аргументы.

        Returns:
            None
        """
        contract = self.get_object()
        if contract.document:
            contract.document.delete(save=False)
        return super().delete(request, *args, **kwargs)

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список контрактов.
        """
        return redirect(reverse_lazy("contract:contract_list"))
