from django import forms
from .models import Product
from typing import Type


class ProductForm(forms.ModelForm):
    """
    Форма для создания или редактирования продукта.
    """
    class Meta:
        """
        Метаданные формы.

        Attributes:
            model (Type[Product]): Связанная модель.
            fields (list[str]): Поля, доступные для редактирования.
        """
        model: Type[Product] = Product
        fields: list[str] = ['name', 'description', 'cost']
