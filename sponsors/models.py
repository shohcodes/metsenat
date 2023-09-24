from core.models import TimeStampedModel
from django.db import models
from sponsors.choices import SponsorTypeChoices, SponsorStatusChoices, SponsorPaymentTypeChoices


class Sponsor(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=SponsorTypeChoices.choices)
    phone_number = models.CharField(max_length=9)
    status = models.CharField(max_length=20, choices=SponsorStatusChoices.choices, default=SponsorStatusChoices.new)
    organization = models.CharField(max_length=255, blank=True, null=True)
    payment_amount = models.FloatField()
    payment_type = models.CharField(max_length=20, choices=SponsorPaymentTypeChoices.choices)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"

    def __str__(self):
        return f"{self.full_name}"
