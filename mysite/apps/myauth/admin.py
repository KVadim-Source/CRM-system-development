from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Админский интерфейс для модели пользователя.

    Этот класс настраивает отображение и поведение модели пользователя
    в административной панели Django.
    """
    list_display = ("username", "email", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name", "email")}),
        ("Права доступа", {'fields': ("is_active", "is_staff", "is_superuser", "groups")}),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )
