from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sponsors.choices import SponsorTypeChoices
from sponsors.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class SponsorListSerializer(serializers.ModelSerializer):
    spent_amount = serializers.SerializerMethodField("get_spent_amount", read_only=True)

    class Meta:
        model = Sponsor
        fields = ['id', 'full_name', 'phone_number', 'payment_amount', 'spent_amount', 'created_at', 'status']

    def get_spent_amount(self, obj):
        return 0


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'full_name', 'phone_number', 'payment_amount', 'organization', 'status', 'created_at']


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        exclude = [
            "status",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        if attrs.get("type") == SponsorTypeChoices.legal_entity.value:
            if not attrs.get("organization"):
                raise ValidationError(
                    f"Organization is required for legal entities!"
                )
        elif attrs.get("type") == SponsorTypeChoices.individual_person.value:
            attrs["organization"] = None
        return attrs


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        exclude = [
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        if attrs.get("type") == SponsorTypeChoices.legal_entity.value:
            if not attrs.get("organization"):
                raise ValidationError(
                    f"Organization is required for legal entities!"
                )
        elif attrs.get("type") == SponsorTypeChoices.individual_person.value:
            attrs["organization"] = None
        return attrs
