from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        permissions = [
            ("can_view_product", "Может просматривать продукт"),
            ("can_add_product", "Может добавлять продукт"),
            ("can_change_product", "Может изменять продукт"),
            ("can_delete_product", "Может удалять продукт"),
        ]

    def __str__(self):
        return self.name
