from db.animals.models import AnimalStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership


def delete_animal(owner_id, animal_id):
    owner = UserStorage.get_by_id(owner_id)
    animal = AnimalStorage.get_by_id(animal_id)
    if owner != animal:
        raise InvalidOwnership
    return AnimalStorage.delete(animal)
