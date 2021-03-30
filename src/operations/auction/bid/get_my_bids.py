from db.auction.models import BidStorage
from db.core.models import UserStorage


def get_my_bids(bidder_id):
    bidder = UserStorage.get_by_id(bidder_id)
    return BidStorage.get_by_bidder(bidder)
