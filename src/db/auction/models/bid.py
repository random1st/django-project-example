from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from db.auction.models import Lot
from db.core.models import BaseUser, BaseModel


class Bid(BaseModel):
    bidder = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='bids')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], decimal_places=2, max_digits=10)
    accepted = models.NullBooleanField(null=True, db_index=True)

    class Meta:
        unique_together = (
            ('lot', 'bidder'),
            ('lot', 'accepted')
        )
