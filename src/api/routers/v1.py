from django.urls import path
from rest_framework.routers import DefaultRouter

from api.resources.user import balance
from api.resources.animals import animal
from api.resources.auction import lot, bid
from api.resources.token import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register('auction/bid', bid.BidViewset, bid.UpdatePriceBidViewset)
router.register('auction/bid', bid.AcceptBidViewset)
router.register('auction/lot', lot.LotViewset)
router.register('auction/lot', lot.LotForSaleViewset)
router.register('animals/animal', animal.AnimalViewSet)
router.register('user/balance', balance.UserBalanceViewset)

api_urlpatterns = router.urls

api_urlpatterns += [
    path('api/v1/jwt/obtain-token/', obtain_jwt_token),
    path('api/v1/jwt/refresh-token/', refresh_jwt_token),
    path('api/v1/jwt/verify-token/', verify_jwt_token),
]
