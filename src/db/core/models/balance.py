from django.db import models

from db.core.models import BaseModel, BaseUser


class UserBalance(BaseModel):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='balance')
    value = models.DecimalField(default=0, decimal_places=2, max_digits=10)
