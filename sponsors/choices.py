from django.db import models


class SponsorTypeChoices(models.TextChoices):
    legal_entity = ('legal_entity', 'Yuridik shaxs')
    individual_person = ('individual_person', 'Jismoniy shaxs')


class SponsorStatusChoices(models.TextChoices):
    new = ('new', 'Yangi')
    in_moderation = ('in_moderation', 'Moderatsiyada')
    confirmed = ('confirmed', 'Tasdiqlangan')
    denied = ('denied', 'Rad qilingan')


class SponsorPaymentTypeChoices(models.TextChoices):
    transfer_money = ('transfer_money', 'Pul kochirish')
    by_card = ('by_card', 'Plastik karta')
    cash = ('cash', 'Naqd pul')
