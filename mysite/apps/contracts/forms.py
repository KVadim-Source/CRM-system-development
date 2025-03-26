from typing import Type

from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    """
    Форма для создания или редактирования контракта.
    """

    class Meta:
        """
        Метаданные формы.

        Attributes:
            model (Type[Contract]): Модель контракта.
            fields (list[str]): Поля, которые будут отображаться в форме.
        """

        model: type[Contract] = Contract
        fields: list[str] = [
            "name",
            "product",
            "document",
            "start_date",
            "end_date",
            "price"
        ]
