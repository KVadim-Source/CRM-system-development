from django.db import models
from apps.leads.models import Lead
from apps.ads.models import Advertisement


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, verbose_name='Лид')
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='customers',
        verbose_name='Рекламная кампания'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Активный клиент'
        verbose_name_plural = 'Активные клиенты'
        permissions = [
            ("can_view_customer", "Может просматривать клиентов"),
            ("can_add_customer", "Может добавлять клиентов"),
            ("can_change_customer", "Может изменять клиентов"),
            ("can_delete_customer", "Может удалять клиентов"),
        ]

    def __str__(self):
        return f'{self.lead.last_name} {self.lead.first_name}'
