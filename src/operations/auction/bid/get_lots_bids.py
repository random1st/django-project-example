from db.auction.models import BidStorage, LotStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership


def get_lots_bid(owner_id, lot_id):
    owner = UserStorage.get_by_id(owner_id)
    lot = LotStorage.get_by_id(lot_id)
    if lot.owner != owner:
        raise InvalidOwnership
    return BidStorage.get_by_lot(lot)
