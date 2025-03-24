from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Contract


@receiver(post_delete, sender=Contract)
def delete_contract_file(sender, instance, **kwargs):
    if instance.document:
        instance.document.delete(save=False)
