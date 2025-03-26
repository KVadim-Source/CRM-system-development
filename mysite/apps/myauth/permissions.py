from rest_framework.permissions import BasePermission


class RolePermission(BasePermission):
    """
    Базовый класс для разрешений, основанных на ролях.

    Attributes:
        role (str): Роль, для которой проверяется разрешение.
    """
    role: str

    def has_permission(self, request, view) -> bool:
        """
        Проверяет, имеет ли пользователь разрешение на доступ.

        Args:
            request: Запрос.
            view: Представление.

        Returns:
            bool: True, если пользователь имеет указанную роль, False иначе.
        """
        return request.user.role == self.role


class IsAdmin(RolePermission):
    """
    Разрешение для администраторов.
    """
    role = 'admin'


class IsOperator(RolePermission):
    """
    Разрешение для операторов.
    """
    role = 'operator'


class IsMarketer(RolePermission):
    """
    Разрешение для маркетологов.
    """
    role = 'marketer'


class IsManager(RolePermission):
    """
    Разрешение для менеджеров.
    """
    role = 'manager'
