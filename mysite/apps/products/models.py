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
            permissions (list[tuple]): Кастомные разрешения для модели.
        """

        verbose_name: str = "Услуга"
        verbose_name_plural: str = "Услуги"
        permissions: list[tuple] = [
            ("can_view_product", "Может просматривать продукт"),
            ("can_add_product", "Может добавлять продукт"),
            ("can_change_product", "Может изменять продукт"),
            ("can_delete_product", "Может удалять продукт"),
        ]

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Название продукта.
        """
        return str(self.name)
