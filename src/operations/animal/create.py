from db.animals.models import AnimalStorage
from db.core.models import UserStorage


def create_animal(owner_id, animal_type, breed, nickname):
    owner = UserStorage.get_by_id(owner_id)
    return AnimalStorage.create(owner, animal_type, breed, nickname)
