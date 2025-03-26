from typing import Any
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """
    Форма для входа пользователя.

    Attributes:
        fields (dict): Поля формы, доступные для редактирования.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует форму и добавляет CSS-класс к виджетам полей.

        Args:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
