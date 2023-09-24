from rest_framework.filters import BaseFilterBackend


class SponsorPaymentFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        amount = request.query_params.get('amount')
        if amount:
            queryset = queryset.filter(payment_amount=amount)
        return queryset


class SponsorTypeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
