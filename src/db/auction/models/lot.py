from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from db.animals.models.animal import Animal
from db.core.models import BaseModel
from operations.errors import LotDoesNotExist


class Lot(BaseModel):
    class Status(models.IntegerChoices):
        DRAFT = 0
        PUBLISHED = 1

    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    price = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], decimal_places=2, max_digits=10)


class LotStorage:
    @staticmethod
    def create(animal, price):
        return Lot.objects.create(animal=animal, price=price)

    @staticmethod
    def lot_is_sold(lot):
        return Lot.objects.filter(bids__accepted__isnull == False).exists()

    @staticmethod
    def update_price(lot, price):
        lot.price = price
        lot.save()
        return lot

    @staticmethod
    def publish(lot):
        lot.status = Lot.Status.PUBLISHED
        lot.save()
        return lot

    @staticmethod
    def unpublish(lot):
        lot.status = Lot.Status.DRAFT
        lot.save()
        return lot

    @staticmethod
    def delete(bid):
        bid.delete()

    @staticmethod
    def get_by_id(lot_id):
        try:
            return Lot.objects.get(id=lot_id)
        except Lot.DoesNotExist as e:
            raise LotDoesNotExist from e

    @staticmethod
    def get_by_animal(animal):
        return Lot.objects \
            .filter(animal=animal) \
            .all()

    @staticmethod
    def get_by_owner(owner):
        return Lot.objects \
            .select_related('animal__owner') \
            .filter(animal__owner=owner) \
            .all()

    @staticmethod
    def get_for_sale():
        return Lot.objects \
            .prefetch_related('bids__accepted') \
            .filter(bids__accepted__isnull=True) \
            .all()
