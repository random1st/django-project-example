from decimal import Decimal

from django.core.validators import MinValueValidator

from db.animals.models.animal import Animal
from db.core.models import BaseModel, BaseUser
from django.db import models


class Lot(BaseModel):
    class Status(models.IntegerChoices):
        CREATED = 0
        PUBLISHED = 1

    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.CREATED)
    price = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], decimal_places=2, max_digits=10)
