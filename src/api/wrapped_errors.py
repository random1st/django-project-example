from rest_framework.exceptions import ValidationError, NotFound

from operations.errors import (
    InvalidOwnership, AnimalDoesNotExist, UserBalanceDoesNotFound, BidHasBeenAccepted, LotDoesNotExist,
    LotHasBeenSold
)


def wrap_exceptions(func):
    def func_(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidOwnership:
            raise ValidationError('Forbidden')
        except AnimalDoesNotExist:
            raise NotFound('Animal does not found')
        except UserBalanceDoesNotFound:
            raise NotFound('UserBalance does not exist')
        except BidHasBeenAccepted:
            raise ValidationError('Bid has been already accepted')
        except LotDoesNotExist:
            raise NotFound('Lot is not found')
        except LotHasBeenSold:
            raise ValidationError('Lo has been already sold')

    return func_
