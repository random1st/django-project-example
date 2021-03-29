from django.db import models

from db.core.models import BaseModel, BaseUser


class Animal(BaseModel):
    class AnimalType(models.IntegerChoices):
        CAT = 1
        HEDGEHOG = 2

    owner = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='animals')
    animal_type = models.IntegerField(choices=AnimalType.choices)
    breed = models.TextField()
    nickname = models.TextField()

