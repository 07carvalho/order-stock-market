import uuid

from django.db import models


class Order(models.Model):
    SIDE_OPTIONS = (
        ("buy", "buy"),
        ("sell", "sell"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isin = models.CharField(max_length=12, null=False, blank=False)
    limit_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=False
    )
    side = models.CharField(max_length=4, choices=SIDE_OPTIONS, null=False, blank=False)
    valid_until = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    class Meta:
        app_label = "orders"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.isin}: {self.side} {self.quantity}"
