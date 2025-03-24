from django.db import models

from products.models import Product


class Advertisement(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Услуга')
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Бюджет')

    class Meta:
        verbose_name = 'Рекламная кампания'
        verbose_name_plural = 'Рекламные кампании'
        permissions = [
            ("can_view_advertisement", "Может просматривать рекламные компании"),
            ("can_add_advertisement", "Может добавлять рекламные компании"),
            ("can_change_advertisement", "Может изменять рекламные компании"),
            ("can_delete_advertisement", "Может удалять рекламные компании"),
        ]

    def __str__(self):
        return self.name

    def leads_count(self):
        return self.leads.count()

    def customers_count(self):
        return self.customers.count()

    def profit(self):
        if self.budget > 0 and self.contracts.count() > 0:
            total_contract_value = sum([contract.price for contract in self.contracts.all()])
            return total_contract_value / self.budget
        return None
