from django.db import models
from apps.customers.models import Customer
from apps.products.models import Product
from apps.ads.models import Advertisement
from django.urls import reverse


class Contract(models.Model):
    """
    Модель контракта.

    Attributes:
        name (str): Название контракта.
        customer (Customer): Клиент, связанный с контрактом.
        product (Product): Продукт или услуга, связанная с контрактом.
        advertisement (Advertisement | None): Рекламная кампания, связанная с контрактом.
        start_date (date): Дата начала контракта.
        end_date (date): Дата окончания контракта.
        price (Decimal): Цена контракта.
        document (FileField | None): Документ, прикрепленный к контракту.
    """
    name: str = models.CharField(max_length=200, verbose_name='Название')
    customer: Customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
        verbose_name='Клиент'
    )
    product: Product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        verbose_name='Услуга'
    )
    advertisement: Advertisement | None = models.ForeignKey(
        'ads.Advertisement',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='contracts_advertisements',
        verbose_name='Рекламная кампания'
    )
    start_date: models.DateField = models.DateField(verbose_name='Дата начала')
    end_date: models.DateField = models.DateField(verbose_name='Дата окончания')
    price: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    document: models.FileField | None = models.FileField(
        upload_to='media',
        blank=True,
        null=True,
        verbose_name='Документ'
    )

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL-адрес для экземпляра Contract.

        Returns:
            str: URL для просмотра деталей контракта.
        """
        return reverse('contracts:contract_detail', args=[str(self.id)])

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
            permissions (list[tuple]): Кастомные разрешения для модели.
        """
        verbose_name: str = 'Контракт'
        verbose_name_plural: str = 'Контракты'
        permissions: list[tuple[str, str]] = [
            ("can_view_contract", "Может просматривать контракты"),
            ("can_add_contract", "Может добавлять контракты"),
            ("can_change_contract", "Может изменять контракты"),
            ("can_delete_contract", "Может удалять контракты"),
        ]

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Название контракта.
        """
        return str(self.name)

    @property
    def cost(self) -> float:
        """
        Возвращает стоимость контракта.

        Returns:
            float: Цена контракта в виде числа с плавающей точкой.
        """
        return float(self.price)
