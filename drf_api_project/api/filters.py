import django_filters
from api.models import Product, Order
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

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'created_at': ['lt', 'gt', 'exact'],
        }