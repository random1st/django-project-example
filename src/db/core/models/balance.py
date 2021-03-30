from django.db import models

from db.core.models import BaseModel, BaseUser
from operations.errors import UserBalanceDoesNotFound


class UserBalance(BaseModel):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='balance')
    value = models.DecimalField(default=0, decimal_places=2, max_digits=10)


class UserBalanceStorage:
    @staticmethod
    def get_user_balance(user):
        if hasattr(user, 'balance'):
            return UserBalance
        else:
            raise UserBalanceDoesNotFound
