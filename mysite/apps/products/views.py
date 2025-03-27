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

from .forms import ProductForm
from .models import Product


class ProductListView(PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка продуктов.

    Attributes:
        model (Product): Модель данных для представления.
        template_name (str): Шаблон для отображения списка.
        context_object_name (str): Имя переменной контекста
        для списка продуктов.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Product = Product
    template_name: str = "products-list.html"
    context_object_name: str = "products"
    permission_required: str = "products.view_product"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на главную страницу.
        """
        return redirect(reverse_lazy("index"))


class ProductDetailView(PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о продукте.

    Attributes:
        model (Product): Модель данных для представления.
        template_name (str): Шаблон для отображения детальной информации.
        context_object_name (str): Имя переменной контекста
        для объекта продукта.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
    """

    model: Product = Product
    template_name: str = "products-detail.html"
    context_object_name: str = "object"
    permission_required: str = "products.view_product"

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список продуктов.
        """
        return redirect(reverse_lazy("products:product_list"))


class ProductCreateView(PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового продукта.

    Attributes:
        model (Product): Модель данных для представления.
        form_class (ProductForm): Форма для создания нового продукта.
        template_name (str): Шаблон для отображения формы создания.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления
        после успешного создания.
    """

    model: Product = Product
    form_class: ProductForm = ProductForm
    template_name: str = "products-create.html"
    permission_required: str = "products.add_product"
    success_url: str = reverse_lazy("products:product_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список продуктов.
        """
        return redirect(reverse_lazy("products:product_list"))


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего продукта.

    Attributes:
        model (Product): Модель данных для представления.
        form_class (ProductForm): Форма для редактирования продукта.
        template_name (str): Шаблон для отображения формы редактирования.
        context_object_name (str): Имя переменной контекста
        для объекта продукта.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления
        после успешного редактирования.
    """

    model: Product = Product
    form_class: ProductForm = ProductForm
    template_name: str = "products-edit.html"
    context_object_name: str = "object"
    permission_required: str = "products.change_product"
    success_url: str = reverse_lazy("products:product_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список продуктов.
        """
        return redirect(reverse_lazy("products:product_list"))


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления продукта.

    Attributes:
        model (Product): Модель данных для представления.
        template_name (str): Шаблон для отображения подтверждения удаления.
        context_object_name (str): Имя переменной контекста
        для объекта продукта.
        permission_required (str): Необходимое разрешение
        для доступа к представлению.
        success_url (str): URL для перенаправления
        после успешного удаления.
    """

    model: Product = Product
    template_name: str = "products-delete.html"
    context_object_name: str = "object"
    permission_required: str = "products.delete_product"
    success_url: str = reverse_lazy("products:product_list")

    def handle_no_permission(self) -> HttpResponseRedirect:
        """
        Переопределяет поведение при отсутствии разрешения.
        Перенаправляет пользователя на список продуктов.
        """
        return redirect(reverse_lazy("products:product_list"))
