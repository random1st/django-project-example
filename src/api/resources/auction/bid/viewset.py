from requests import Response
from rest_framework import viewsets, permissions, status

from api.resources.auction.bid import BidSerializer, UpdatePriceBidSerializer, AcceptBidSerializer, LotBidSerializer
from api.wrapped_errors import wrap_exceptions
from db.auction.models import Bid
from operations.auction.bid.accept import accept_bid
from operations.auction.bid.create import create_bid
from operations.auction.bid.delete import delete_bid
from operations.auction.bid.get_lots_bids import get_lots_bid
from operations.auction.bid.get_my_bids import get_my_bids
from operations.auction.bid.update_price import update_bid_price


# Bidder

class BidViewset(viewsets.GenericViewSet):
    queryset = Bid.objects.none()
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    @wrap_exceptions
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        if serializer.is_valid(raise_exception=True):
            instance = create_bid(
                bidder_id=request.user.id,
                lot_id=serializer.validated_data['lot_id'],
                price=serializer.validated_data['price'],
            )
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    @wrap_exceptions
    def list(self, request, *args, **kwargs):
        queryset = get_my_bids(bidder_id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    @wrap_exceptions
    def destroy(self, request, pk=None, *args, **kwargs):
        delete_bid(
            bidder_id=request.user.id,
            bid_id=pk,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePriceBidViewset(viewsets.GenericViewSet):
    queryset = Bid.objects.none()
    serializer_class = UpdatePriceBidSerializer
    permission_classes = [permissions.IsAuthenticated]

    @wrap_exceptions
    def partial_update(self, request, pk=None, *args, **kwargs):
        serializer = self.get_serializer(request.data, partial_update=True)
        if serializer.is_valid(raise_exception=True):
            instance = update_bid_price(
                bidder_id=request.user.id,
                bid_id=pk,
                price=serializer.validated_data['price']
            )
            serializer = self.get_serializer(instance)
            return Response(serializer.data)


# Lot owner


class AcceptBidViewset(viewsets.GenericViewSet):
    queryset = Bid.objects.none()
    serializer_class = AcceptBidSerializer
    permission_classes = [permissions.IsAuthenticated]

    @wrap_exceptions
    def partial_update(self, request, pk=None, *args, **kwargs):
        serializer = self.get_serializer(request.data, partial_update=True)
        if serializer.is_valid(raise_exception=True):
            instance = accept_bid(owner_id=request.user.id, bid_id=pk)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)


class LotBidViewset(viewsets.GenericViewSet):
    queryset = Bid.objects.none()
    serializer_class = LotBidSerializer
    permission_classes = [permissions.IsAuthenticated]

    @wrap_exceptions
    def list(self, request, lot_id=None, *args, **kwargs):
        queryset = get_lots_bid(owner_id=request.user.id, lot_id=lot_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
