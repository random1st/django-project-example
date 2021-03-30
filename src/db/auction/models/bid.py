from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from rest_framework.fields import BooleanField

from db.auction.models import Lot
from db.core.models import BaseUser, BaseModel
from operations.errors import BidDoesNotExist


class Bid(BaseModel):
    bidder = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='bids')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], decimal_places=2, max_digits=10)
    accepted = models.BooleanField(null=True, db_index=True)

    class Meta:
        unique_together = (
            ('lot', 'bidder'),
            ('lot', 'accepted')
        )


class BidStorage:
    @staticmethod
    def create(bidder, lot, price):
        return Bid.objects.create(bidder=bidder, lot=lot, price=price)

    @staticmethod
    def update_price(bid, price):
        bid.price = price
        bid.save()
        return bid

    @staticmethod
    def delete(bid):
        bid.delete()

    @staticmethod
    def get_by_bidder(bidder):
        qs = Bid.objects \
            .select_for_update() \
            .filter(bidder=bidder) \
            .all()

    @staticmethod
    def accept_by_lot_owner(bid):
        qs = Bid.objects \
            .select_related('lot__owner') \
            .select_for_update() \
            .filter(lot__owner=bid.lot.owner) \
            .all()

        list(qs)
        bid.accepted = True
        bid.save()
        return bid

    @staticmethod
    def get_by_id(bid_id):
        try:
            return Bid.objects.get(id=bid_id)
        except Bid.DoesNotExist as e:
            raise BidDoesNotExist from e

    @staticmethod
    def get_by_lot(lot):
        return Bid.objects.select_related("lot__owner").filter(lot=lot)

    @staticmethod
    def get_by_owner(owner):
        return Bid.objects \
            .select_related('lot__animal__owner') \
            .filter(lot__animal__owner=owner) \
            .all()

    @staticmethod
    def get_lot_owner(bid):
        lot = Lot.objects \
            .select_related('lot__owner') \
            .filter(bid=bid).first()
        if lot:
            return lot.owner
