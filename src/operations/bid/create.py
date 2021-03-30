from db.auction.models import LotStorage, BidStorage
from db.core.models import UserStorage


def create_bid(bidder_id, lot_id, price):
    bidder = UserStorage.get_by_id(bidder_id)
    lot = LotStorage.get_by_id(lot_id)
    return BidStorage.create(bidder, lot, price)
