from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AdvertisementForm
from .models import Advertisement, AdvertisementQuerySet


class AdvertisementListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка рекламных кампаний.

    Attributes:
        model (Advertisement): Модель данных для отображения.
        template_name (str): Шаблон для отображения списка.
        context_object_name (str): Имя переменной контекста
        для списка рекламных кампаний.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Advertisement = Advertisement
    template_name: str = "ads-list.html"
    context_object_name: str = "ads"
    permission_required: str = "ads.can_view_advertisement"


class AdvertisementStatisticView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения статистики рекламных кампаний.

    Attributes:
        model (Advertisement): Модель данных для отображения.
        template_name (str): Шаблон для отображения статистики.
        context_object_name (str): Имя переменной контекста
        для списка рекламных кампаний.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Advertisement = Advertisement
    template_name: str = "ads-statistic.html"
    context_object_name: str = "ads"
    permission_required: str = "ads.can_view_advertisement"

    def get_queryset(self) -> AdvertisementQuerySet:
        """
        Возвращает QuerySet с дополнительными статистическими данными.

        Returns:
            AdvertisementQuerySet: QuerySet с аннотированными данными.
        """
        return Advertisement.objects.with_stats()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = self.get_queryset()
        return context


class AdvertisementDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о рекламной кампании.

    Attributes:
        model (Advertisement): Модель данных для отображения.
        template_name (str): Шаблон для отображения детальной информации.
        context_object_name (str): Имя переменной контекста
        для рекламной кампании.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Advertisement = Advertisement
    template_name: str = "ads-detail.html"
    context_object_name: str = "object"
    permission_required: str = "ads.can_view_advertisement"


class AdvertisementCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания новой рекламной кампании.

    Attributes:
        model (Advertisement): Модель данных для создания.
        form_class (AdvertisementForm): Форма для создания рекламной кампании.
        template_name (str): Шаблон для отображения формы создания.
        success_url (str): URL для перенаправления после успешного создания.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Advertisement = Advertisement
    form_class: AdvertisementForm = AdvertisementForm
    template_name: str = "ads-create.html"
    success_url: str = reverse_lazy("ads:advertisement_list")
    permission_required: str = "ads.can_add_advertisement"


class AdvertisementUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования рекламной кампании.

    Attributes:
        model (Advertisement): Модель данных для редактирования.
        form_class (AdvertisementForm): Форма для редактирования
        рекламной кампании.
        template_name (str): Шаблон для отображения формы редактирования.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Advertisement = Advertisement
    form_class: AdvertisementForm = AdvertisementForm
    template_name: str = "ads-edit.html"
    permission_required: str = "ads.can_change_advertisement"


class AdvertisementDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления рекламной кампании.

    Attributes:
        model (Advertisement): Модель данных для удаления.
        template_name (str): Шаблон для подтверждения удаления.
        success_url (str): URL для перенаправления после успешного удаления.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Advertisement = Advertisement
    template_name: str = "ads-delete.html"
    success_url: str = reverse_lazy("ads:advertisement_list")
    permission_required: str = "ads.can_delete_advertisement"
