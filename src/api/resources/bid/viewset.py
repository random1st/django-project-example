from django.db.models import Q
from rest_framework import viewsets, permissions

from db.auction.models import Bid


class BidViewset(viewsets.GenericViewSet,
                 viewsets.mixins.ListModelMixin,
                 viewsets.mixins.UpdateModelMixin,
                 viewsets.mixins.DestroyModelMixin):

    queryset = Bid.objects.none()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Bid.objects.select_related(
            'lot__animal__owner_id'
        ).filter(
            Q(bidder=user) | Q(lot__animal__owner_id=user.id)
        ).all()

    class Meta:
        model = Bid
        fields = '__all__'
