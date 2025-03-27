from typing import Type

from django import forms

from apps.contracts.models import Contract

from .models import Customer


class CustomerForm(forms.ModelForm):
    """
    Форма для создания или редактирования клиента.

    Attributes:
        contract (ModelChoiceField): Поле выбора контракта.
    """

    contract = forms.ModelChoiceField(
        queryset=Contract.objects.all(), required=True, label="Контракт"
    )

    class Meta:
        """
        Метаданные формы.

        Attributes:
            model (Type[Customer]): Связанная модель.
            fields (list[str]): Поля, доступные для редактирования.
        """

        model: Type[Customer] = Customer
        fields: list[str] = ["lead", "contract"]
