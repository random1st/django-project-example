from db.auction.models import LotStorage


def get_lots_for_sale():
    return LotStorage.get_for_sale()
