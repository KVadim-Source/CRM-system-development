from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    """Модель услуги"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class AdCampaign(models.Model):
    """Модель рекламной кампании"""
    name = models.CharField(max_length=200)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    channel = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class PotentialClient(models.Model):
    """Модель потенциального клиента"""
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    ad_campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    """Модель контракта"""
    name = models.CharField(max_length=200)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    document_file = models.FileField(upload_to='contracts/')
    conclusion_date = models.DateField()
    period = models.IntegerField()  # в месяцах
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ActiveClient(models.Model):
    """Модель активного клиента"""
    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def __str__(self):
        return self.potential_client.full_name
