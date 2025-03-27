from django.db import models


class Product(models.Model):
    """
    Модель продукта.

    Attributes:
        name (str): Название продукта.
        description (str): Описание продукта.
        cost (Decimal): Стоимость продукта.
    """

    name: str = models.CharField(max_length=200, verbose_name="Название")
    description: str = models.TextField(verbose_name="Описание")
    cost: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость"
    )

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
        """

        verbose_name: str = "Услуга"
        verbose_name_plural: str = "Услуги"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Название продукта.
        """
        return str(self.name)
