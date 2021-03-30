from db.auction.models import BidStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership, BidHasBeenAccepted


def update_bid_price(bidder_id, bid_id, price):
    bidder = UserStorage.get_by_id(bidder_id)
    bid = BidStorage.get_by_id(bid_id)
    if bidder != bid.bidder:
        raise InvalidOwnership
    if bid.accepted:
        raise BidHasBeenAccepted
    return BidStorage.update_price(bid, price)
