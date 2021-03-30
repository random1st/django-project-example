from db.auction.models import LotStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership, LotHasBeenSold


def delete_lot(owner_id, lot_id):
    owner = UserStorage.get_by_id(owner_id)
    lot = LotStorage.get_by_id(lot_id)
    if owner != lot.owner:
        raise InvalidOwnership
    if not LotStorage.lot_is_sold(lot):
        return LotStorage.delete
    else:
        raise LotHasBeenSold
