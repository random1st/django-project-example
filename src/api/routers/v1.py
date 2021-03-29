from django.urls import path
from rest_framework.routers import DefaultRouter
from api.resources.token import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from api.resources import bid, lot, animal, balance

router = DefaultRouter()
router.register('bid', bid.BidViewset)
router.register('lot', lot.LotViewset)
router.register('animal', animal.AnimalViewset)
router.register('balance', balance.UserBalanceViewset)

api_urlpatterns = router.urls

api_urlpatterns += [
    path('api/v1/jwt/obtain-token/', obtain_jwt_token),
    path('api/v1/jwt/refresh-token/', refresh_jwt_token),
    path('api/v1/jwt/verify-token/', verify_jwt_token),
]
