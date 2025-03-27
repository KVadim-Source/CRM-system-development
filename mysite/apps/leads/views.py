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

from .forms import LeadForm
from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка лидов.

    Attributes:
        model (Lead): Модель данных для представления.
        template_name (str): Шаблон для отображения списка.
        context_object_name (str): Имя переменной контекста
        для списка лидов.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Lead = Lead
    template_name: str = "leads-list.html"
    context_object_name: str = "leads"
    permission_required: str = "leads.view_lead"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на главную страницу.
        """
        return redirect(reverse_lazy("index"))


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о лиде.

    Attributes:
        model (Lead): Модель данных для представления.
        template_name (str): Шаблон для отображения детальной информации.
        context_object_name (str): Имя переменной контекста
        для лида.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Lead = Lead
    template_name: str = "leads-detail.html"
    context_object_name: str = "object"
    permission_required: str = "leads.view_lead"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список лидов.
        """
        return redirect(reverse_lazy("leads:lead_list"))


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового лида.

    Attributes:
        model (Lead): Модель данных для представления.
        form_class (LeadForm): Форма для создания нового лида.
        template_name (str): Шаблон для отображения формы создания.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления после успешного создания.
    """

    model: Lead = Lead
    form_class: LeadForm = LeadForm
    template_name: str = "leads-create.html"
    permission_required: str = "leads.add_lead"
    success_url: str = reverse_lazy("leads:lead_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список лидов.
        """
        return redirect(reverse_lazy("leads:lead_list"))


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего лида.

    Attributes:
        model (Lead): Модель данных для представления.
        form_class (LeadForm): Форма для редактирования лида.
        template_name (str): Шаблон для отображения формы редактирования.
        context_object_name (str): Имя переменной контекста для лида.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления после успешного редактирования.
    """

    model: Lead = Lead
    form_class: LeadForm = LeadForm
    template_name: str = "leads-edit.html"
    context_object_name: str = "object"
    permission_required: str = "leads.change_lead"
    success_url: str = reverse_lazy("leads:lead_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список лидов.
        """
        return redirect(reverse_lazy("leads:lead_list"))


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления лида.

    Attributes:
        model (Lead): Модель данных для представления.
        template_name (str): Шаблон для отображения подтверждения удаления.
        context_object_name (str): Имя переменной контекста для лида.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления после успешного удаления.
    """

    model: Lead = Lead
    template_name: str = "leads-delete.html"
    context_object_name: str = "object"
    permission_required: str = "leads.delete_lead"
    success_url: str = reverse_lazy("leads:lead_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список лидов.
        """
        return redirect(reverse_lazy("leads:lead_list"))
