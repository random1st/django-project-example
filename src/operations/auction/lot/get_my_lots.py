from db.auction.models import LotStorage
from db.core.models import UserStorage


def get_my_lots(owner_id):
    owner = UserStorage.get_by_id(owner_id)
    return LotStorage.get_by_owner(owner)
