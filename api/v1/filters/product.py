import django_filters
from apps.product.models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(
        field_name='category__id',
        lookup_expr='iexact',
    )
    tag = django_filters.NumberFilter(
        field_name='tags__id',
        lookup_expr='iexact'
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Minimum Price'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Maximum Price'
    )
    name_uz = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name='name_uz'
    )
    name_ru = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name='name_ru'
    )
    name_en = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name='name_en'
    )

    class Meta:
        model = Product
        fields = ['category', 'tags', 'name_uz', 'name_ru', 'name_en', 'tag', 'min_price', 'max_price', ]
