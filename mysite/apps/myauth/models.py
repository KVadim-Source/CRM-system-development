from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя с расширенными полями.

    Attributes:
        role (str): Роль пользователя.
        groups (ManyToManyField): Группы, в которых состоит пользователь.
        user_permissions (ManyToManyField): Разрешения,
        назначенные пользователю напрямую.
    """

    ROLE_CHOICES: tuple = (
        ("admin", "Admin"),
        ("operator", "Operator"),
        ("marketer", "Marketer"),
        ("manager", "Manager"),
    )

    role: str = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="operator"
    )

    groups: models.ManyToManyField = models.ManyToManyField(
        Group, related_name="custom_user_set", blank=True
    )

    user_permissions: models.ManyToManyField = models.ManyToManyField(
        Permission, related_name="custom_user_permissions_set", blank=True
    )

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели
            во множественном числе.
        """

        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Имя пользователя.
        """
        return str(self.username)
