from datetime import datetime

from rest_framework import exceptions, serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    # following LM documentation. in swagger will appear as string due precision
    limit_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Order
        fields = "__all__"

    def validate_limit_price(self, value):
        if not value > 0:
            raise exceptions.ValidationError(
                detail="Limit price must be greater than zero."
            )
        return value

    def validate_valid_until(self, value):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        valid_until = datetime.fromtimestamp(value)
        if valid_until < today:
            raise exceptions.ValidationError(detail="Dates in the past are invalid")
        return value

    def validate_quantity(self, value):
        if not value > 0:
            raise exceptions.ValidationError(detail="Quantity must be greater than zero.")
        return value
