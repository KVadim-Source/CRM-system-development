from django.db import models
from apps.customers.models import Customer
from apps.products.models import Product
from apps.ads.models import Advertisement


class Contract(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Услуга')
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='contracts',
        verbose_name='Рекламная кампания'
    )
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    document = models.FileField(upload_to='media', blank=True, null=True, verbose_name='Документ')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
        permissions = [
            ("can_view_contract", "Может просматривать контракты"),
            ("can_add_contract", "Может добавлять контракты"),
            ("can_change_contract", "Может изменять контракты"),
            ("can_delete_contract", "Может удалять контракты"),
        ]

    def __str__(self):
        return self.name

    @property
    def cost(self):
        return self.price
