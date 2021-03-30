from db.auction.models import BidStorage, LotStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership


def accept_bid(owner_id, bid_id):
    owner = UserStorage.get_by_id(owner_id)
    bid = BidStorage.get_by_id(bid_id)
    real_owner = BidStorage.get_lot_owner(bid)

    if owner != real_owner:
        raise InvalidOwnership
    if LotStorage.lot_is_sold(bid.lot):
        raise
    return BidStorage.accept_by_lot_owner(bid)
