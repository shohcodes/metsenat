from rest_framework.filters import BaseFilterBackend


class StudentTypeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        type = request.query_params.get('type')
        if type:
            queryset = queryset.filter(type=type)
        return queryset


class StudentInstituteFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        institute = request.query_params.get('institute')
        if institute:
            queryset = queryset.filter(institute=institute)
        return queryset
