from typing import Type

from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    """
    Форма для создания или редактирования потенциального клиента.
    """

    class Meta:
        """
        Метаданные формы.

        Attributes:
            model (Type[Lead]): Связанная модель.
            fields (list[str]): Поля, доступные для редактирования.
        """

        model: Type[Lead] = Lead
        fields: list[str] = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "advertisement",
        ]
