import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")  # gte greater than or equal to
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")  # less than or equal to
    note = CharFilter(field_name="note", lookup_expr="icontains")
    class Meta:
        model = Order
        fields = "__all__"  # selecting all the fields in the class order
        exclude = ['customer', 'date_created']
