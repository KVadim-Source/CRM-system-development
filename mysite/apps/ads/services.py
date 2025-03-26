from .models import Advertisement
from typing import Dict


class AdvertisementStatsService:
    """
    Сервис для получения статистики рекламных кампаний.
    """

    @classmethod
    def get_campaign_stats(cls, campaign_id: int) -> Dict[str, int | float]:
        """
        Возвращает статистику рекламной кампании по ее ID.

        Args:
            campaign_id (int): ID рекламной кампании.

        Returns:
            Dict[str, int | float]: Словарь с ключами:
                - leads_count (int): Количество потенциальных клиентов.
                - customers_count (int): Количество активных клиентов.
                - profit (float): Соотношение контрактов к затратам.

        Raises:
            Advertisement.DoesNotExist: Если кампания с указанным ID не существует.
        """
        campaign = Advertisement.objects.with_stats().get(pk=campaign_id)
        return {
            'leads_count': campaign.leads_count,
            'customers_count': campaign.customers_count,
            'profit': campaign.profit
        }
