from django import forms
from .models import Contract
from typing import Type


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
            widgets (dict): Виджеты для настройки отображения полей.
        """
        model: Type[Contract] = Contract
        fields: list[str] = [
            'name', 'customer', 'product', 'advertisement',
            'start_date', 'end_date', 'price', 'document'
        ]
        widgets: dict[str, forms.DateInput] = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
