from rest_framework import mixins, viewsets

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
