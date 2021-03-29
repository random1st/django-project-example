from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from db.auction.models import Bid, Lot


class BidSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        lot_id = validated_data['lot_id']
        try:
            lot = Lot.objects.get(id=lot_id)
        except Lot.DoesNotExists:
            raise ValidationError('Unknown lot')

        if lot.bids.filter(accepted=True).exists():
            raise ValidationError('Auction has already ended')

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.accepted:
            raise PermissionDenied('Can\'t update already accepted bid')

    class Meta:
        model = Bid
        fields = '__all__'
