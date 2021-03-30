from db.animals.models import AnimalStorage


def get_by_id(animal_id):
    return AnimalStorage.get_by_id(animal_id)
