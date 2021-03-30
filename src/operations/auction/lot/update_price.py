from db.auction.models import LotStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership
from operations.auction.lot import LotHasBeenSold


def update_lot_price(owner_id, bid_id, price):
    owner = UserStorage.get_by_id(owner_id)
    lot = LotStorage.get_by_id(bid_id)
    if owner != lot.owner:
        raise InvalidOwnership
    if LotStorage.lot_is_sold(lot):
        raise LotHasBeenSold
    return LotStorage.update_price(lot, price)
