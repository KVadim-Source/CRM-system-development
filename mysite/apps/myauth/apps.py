from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MyauthConfig(AppConfig):
    """
    Конфигурация приложения "Аутентификация".

    Attributes:
        default_auto_field (str): Тип
        автоматически генерируемого первичного ключа.
        name (str): Путь к приложению.
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.myauth"

    def ready(self):
        from django.contrib.auth.models import Group, Permission

        def create_groups(sender, **kwargs):
            """
            Создание групп пользователей и назначение им разрешений.

            Attributes:
                group_permissions (dict): Словарь с группами и их разрешениями.
            """
            group_permissions = {
                'Operator': [
                    "view_lead", "add_lead", "change_lead",
                    "view_advertisement"
                ],
                'Marketer': [
                    "view_product", "add_product", "change_product",
                    "view_advertisement", "add_advertisement", "change_advertisement"
                ],
                'Manager': [
                    "view_contract", "add_contract", "change_contract",
                    "view_lead", "view_customer", "add_customer",
                    "change_customer", "view_advertisement"
                ]
            }

            for group_name, permissions in group_permissions.items():
                group, created = Group.objects.get_or_create(name=group_name)

                for codename in permissions:
                    try:
                        perm = Permission.objects.get(codename=codename)
                        group.permissions.add(perm)
                    except Permission.DoesNotExist:
                        print(f"Permission {codename} does not exist yet.")

        post_migrate.connect(create_groups, sender=self)
