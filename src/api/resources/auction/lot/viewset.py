from requests import Response
from rest_framework import viewsets, permissions, status

from api.resources.auction.lot import LotSerializer, LotForSaleSerializer
from api.wrapped_errors import wrap_exceptions
from db.auction.models import Lot
from operations.auction.lot import create_lot
# Lot owner
from operations.auction.lot import delete_lot
from operations.auction.lot import get_my_lots


class LotViewset(viewsets.GenericViewSet):
    serializer_class = LotSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lot.objects.none()

    @wrap_exceptions
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        if serializer.is_valid(raise_exception=True):
            instance = create_lot(
                owner_id=request.user.id,
                animal_id=serializer.validated_data['animal_id'],
                price=serializer.validated_data['price'],
            )
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    @wrap_exceptions
    def list(self, request, *args, **kwargs):
        queryset = get_my_lots(owner_id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    @wrap_exceptions
    def destroy(self, request, pk=None, *args, **kwargs):
        delete_lot(
            owner_id=request.user.id,
            lot_id=pk,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)


# Bidder


class LotForSaleViewset(viewsets.GenericViewSet):
    serializer_class = LotForSaleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lot.objects.none()

    @wrap_exceptions
    def list(self, request, *args, **kwargs):
        queryset = get_my_lots(owner_id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
