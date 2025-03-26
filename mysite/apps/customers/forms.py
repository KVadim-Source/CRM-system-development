from django import forms
from .models import Customer
from apps.leads.models import Lead
from typing import Type


class CustomerForm(forms.ModelForm):
    """
    Форма для создания или редактирования клиента.

    Attributes:
        lead (ModelChoiceField): Поле выбора потенциального клиента.
    """
    lead: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=Lead.objects.all(),
        label='Лид'
    )

    class Meta:
        """
        Метаданные формы.

        Attributes:
            model (Type[Customer]): Связанная модель.
            fields (list[str]): Поля, доступные для редактирования.
        """
        model: Type[Customer] = Customer
        fields: list[str] = ['lead', 'advertisement']
