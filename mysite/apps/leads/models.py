from django.db import models
from apps.ads.models import Advertisement


class Lead(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='leads',
        verbose_name='Рекламная кампания',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
        permissions = [
            ("can_view_lead", "Может просматривать лид"),
            ("can_add_lead", "Может добавлять лид"),
            ("can_change_lead", "Может изменять лид"),
            ("can_delete_lead", "Может удалять лид"),
        ]

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
