from db.animals.models import AnimalStorage
from db.auction.models import LotStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership


def create_lot(owner_id, animal_id, price):
    animal = AnimalStorage.get_by_id(animal_id)
    owner = UserStorage.get_by_id(owner_id)
    if owner != animal.owner:
        raise InvalidOwnership
    return LotStorage.create(animal, price)
