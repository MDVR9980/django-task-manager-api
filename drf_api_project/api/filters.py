import django_filters
from api.models import Product
from rest_framework import filters

class InStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(stock__gt=0)
        # return queryset.exclude(stock__gt=0)


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        # fields = ('name', 'price',)
        fields = {
            # 'name': ['exact', 'contains'],
            'name': ['iexact', 'icontains'],
            'price': ['exact', 'lt', 'gt', 'range'],
        }