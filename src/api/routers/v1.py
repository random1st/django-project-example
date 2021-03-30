from django.urls import path
from rest_framework.routers import DefaultRouter

from api.resources import bid, lot, animal, balance
from api.resources.token import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register('bidder/bid', bid.BidViewset, bid.UpdatePriceBidViewset)
router.register('owner/bid', bid.AcceptBidViewset)
router.register('owner/lot', lot.LotViewset)
router.register('bidder/lot', lot.LotForSaleViewset)
router.register('owner/animal', animal.AnimalViewSet)
router.register('user/balance', balance.UserBalanceViewset)

api_urlpatterns = router.urls

api_urlpatterns += [
    path('api/v1/jwt/obtain-token/', obtain_jwt_token),
    path('api/v1/jwt/refresh-token/', refresh_jwt_token),
    path('api/v1/jwt/verify-token/', verify_jwt_token),
]
