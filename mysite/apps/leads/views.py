from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import LeadForm
from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка потенциальных клиентов.

    Attributes:
        model (Lead): Модель данных для представления.
        template_name (str): Шаблон для отображения списка.
        context_object_name (str): Имя переменной контекста
        для списка потенциальных клиентов.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Lead = Lead
    template_name: str = "leads-list.html"
    context_object_name: str = "leads"
    permission_required: str = "leads.can_view_lead"


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о потенциальном клиенте.

    Attributes:
        model (Lead): Модель данных для представления.
        template_name (str): Шаблон для отображения детальной информации.
        context_object_name (str): Имя переменной контекста
        для потенциального клиента.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Lead = Lead
    template_name: str = "leads-detail.html"
    context_object_name: str = "object"
    permission_required: str = "leads.can_view_lead"


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового потенциального клиента.

    Attributes:
        model (Lead): Модель данных для представления.
        form_class (LeadForm): Форма для создания нового потенциального клиента.
        template_name (str): Шаблон для отображения формы создания.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления после успешного создания.
    """

    model: Lead = Lead
    form_class: LeadForm = LeadForm
    template_name: str = "leads-create.html"
    permission_required: str = "leads.can_add_lead"
    success_url: str = reverse_lazy("leads:lead_list")


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего потенциального клиента.

    Attributes:
        model (Lead): Модель данных для представления.
        form_class (LeadForm): Форма для редактирования потенциального клиента.
        template_name (str): Шаблон для отображения формы редактирования.
        context_object_name (str): Имя переменной контекста
        для потенциального клиента.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления после успешного редактирования.
    """

    model: Lead = Lead
    form_class: LeadForm = LeadForm
    template_name: str = "leads-edit.html"
    context_object_name: str = "object"
    permission_required: str = "leads.can_change_lead"
    success_url: str = reverse_lazy("leads:lead_list")


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления потенциального клиента.

    Attributes:
        model (Lead): Модель данных для представления.
        template_name (str): Шаблон для отображения подтверждения удаления.
        context_object_name (str): Имя переменной контекста
        для потенциального клиента.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления после успешного удаления.
    """

    model: Lead = Lead
    template_name: str = "leads-delete.html"
    context_object_name: str = "object"
    permission_required: str = "leads.can_delete_lead"
    success_url: str = reverse_lazy("leads:lead_list")
