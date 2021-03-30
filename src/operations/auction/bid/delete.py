from db.auction.models import BidStorage
from db.core.models import UserStorage
from operations.errors import InvalidOwnership


def delete_bid(bidder_id, bid_id):
    bidder = UserStorage.get_by_id(bidder_id)
    bid = BidStorage.get_by_id(bid_id)
    if bid.bidder != bidder:
        raise InvalidOwnership
    return BidStorage.delete(bid)
