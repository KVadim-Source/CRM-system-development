from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.ads.models import Advertisement
from apps.customers.models import Customer
from apps.leads.models import Lead
from apps.products.models import Product

from .permissions import IsAdmin


class UserView(APIView):
    """
    Представление для работы с пользователями.

    Attributes:
        permission_classes (list): Список разрешений
        для доступа к представлению.
    """

    permission_classes: list = [IsAdmin]

    def get(self) -> Response:
        """
        Возвращает список пользователей.

        Returns:
            Response: Ответ с сообщением.
        """
        return Response({"message": "Users list"})


def custom_logout(request: HttpRequest) -> HttpResponse:
    """
    Выполняет выход пользователя из системы.

    Args:
        request (HttpRequest): Запрос.

    Returns:
        HttpResponse: Перенаправление на страницу входа
        или сообщение об ошибке.
    """
    try:
        logout(request)
        return redirect("/accounts/login/")
    except Exception:
        return HttpResponse("Ошибка при выходе из системы", status=500)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """
    Отображает главную страницу с количеством объектов в системе.

    Args:
        request (HttpRequest): Запрос.

    Returns:
        HttpResponse: Ответ с шаблоном главной страницы
        или сообщение об ошибке.
    """
    try:
        products_count: int = Product.objects.count()
        advertisements_count: int = Advertisement.objects.count()
        leads_count: int = Lead.objects.count()
        customers_count: int = Customer.objects.count()

        context: dict = {
            "products_count": products_count,
            "advertisements_count": advertisements_count,
            "leads_count": leads_count,
            "customers_count": customers_count,
        }

        return render(request, "users/index.html", context)
    except Exception:
        return HttpResponse("Ошибка при отображении главной страницы", status=500)
