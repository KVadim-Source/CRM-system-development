from typing import Type
from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    """
    Форма для создания или редактирования рекламной кампании.
    """
    class Meta:
        """
        Метаданные формы.

        Attributes:
            model (Type[Advertisement]): Модель, связанная с формой.
            fields (list[str]): Поля, доступные для редактирования.
        """
        model: Type[Advertisement] = Advertisement
        fields: list[str] = ['name', 'product', 'channel', 'budget']
