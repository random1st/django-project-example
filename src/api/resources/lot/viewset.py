from rest_framework import viewsets

from db.auction.models import Lot


class LotViewset(viewsets.ModelViewSet):
    queryset = Lot.objects.filter(status=Lot.Status.PUBLISHED).all()

    class Meta:
        model = Lot
        fields = '__all__'
