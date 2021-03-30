from django.db import models

from db.core.models import BaseModel, BaseUser
from operations.errors import AnimalDoesNotExist


class Animal(BaseModel):
    class AnimalType(models.IntegerChoices):
        CAT = 1
        HEDGEHOG = 2

    owner = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='animals')
    animal_type = models.IntegerField(choices=AnimalType.choices)
    breed = models.TextField()
    nickname = models.TextField()


class AnimalStorage:
    @staticmethod
    def create(owner, animal_type, breed, nickname):
        return Animal.objects \
            .create(owner=owner, animal_type=animal_type, breed=breed, nickname=nickname)

    @staticmethod
    def get_by_id(animal_id):
        try:
            return Animal.objects.get(id=animal_id)
        except Animal.DoesNotExist as e:
            raise AnimalDoesNotExist from e

    @staticmethod
    def get_by_owner(owner):
        return Animal.objects.filter(owner=owner)

    @staticmethod
    def get_all():
        return Animal.objects.all()

    @staticmethod
    def delete(animal):
        return animal.delete()
