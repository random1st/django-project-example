class InvalidOwnership(BaseException):
    pass


class AnimalDoesNotExist(BaseException):
    pass


class BidDoesNotExist(BaseException):
    pass


class LotDoesNotExist(BaseException):
    pass


class UserBalanceDoesNotFound(BaseException):
    pass


class UserDoesNotExist(BaseException):
    pass


class BidHasBeenAccepted(BaseException):
    pass


class LotHasBeenSold(BaseException):
    pass
